from rest_framework import serializers
from .models import Customer, CustomerCategory, CustomerCategoryKeyword
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Customer
        fields = ['user', 'first_name', 'last_name', 'email', 'search_intrest_string']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer

class CustomerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = ['id', 'customer', 'category', 'sub_category', 'clicks', 'searches', 'score', 'last_updated']

class CustomerCategoryKeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategoryKeyword
        fields = ['id', 'customer_category', 'keyword', 'clicks', 'searches', 'score', 'last_updated']
