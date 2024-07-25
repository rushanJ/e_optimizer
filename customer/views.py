from rest_framework import viewsets
from .models import Customer, CustomerCategory, CustomerCategoryKeyword
from .serializers import CustomerSerializer, CustomerCategorySerializer, CustomerCategoryKeywordSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerCategoryViewSet(viewsets.ModelViewSet):
    queryset = CustomerCategory.objects.all()
    serializer_class = CustomerCategorySerializer

class CustomerCategoryKeywordViewSet(viewsets.ModelViewSet):
    queryset = CustomerCategoryKeyword.objects.all()
    serializer_class = CustomerCategoryKeywordSerializer


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        print (request.data)
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            token, created = Token.objects.get_or_create(user=customer.user)
            return Response({'token': token.key, 'customer_id': customer.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            customer = Customer.objects.get(user=user)
            return Response({'token': token.key, 'customer_id': customer.id}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)