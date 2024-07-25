from rest_framework import viewsets
from .models import SystemService
from .serializers import SystemServiceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from lib.openai_lib import generate_keywords
from lib.bs import extract_text_from_html
from customer.views import CustomerCategory,Customer,CustomerCategoryKeyword
def check_contains(text1, text2):
    if text1 in text2:
       return True
    else:
        return False

class SystemServiceViewSet(viewsets.ModelViewSet):
    queryset = SystemService.objects.all()
    serializer_class = SystemServiceSerializer


@api_view(['GET'])
def search_by_url_pattern(request):
    # Example usage
    try:
        url = request.GET.get('url')
    except (json.JSONDecodeError, KeyError):
        return Response({'error': 'Invalid JSON or missing url_pattern parameter'}, status=status.HTTP_400_BAD_REQUEST)
    if url:
        return_data=None
        services = SystemService.objects.all()
        for service in services:
            if check_contains( service.url_pattern,url):
                serializer = SystemServiceSerializer(service)  # Serialize individual service
                return_data=serializer.data
            
        if return_data:
            return Response({"is_in_system": 1, "data": return_data}, status=status.HTTP_200_OK)
        else:
            return Response({"is_in_system": 0}, status=status.HTTP_200_OK)
                
    else:
        return Response({'error': 'url parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_user_preference(request):
    
    try:
        item_name = request.GET.get('item_name')
        user_id = int(request.GET.get('user_id'))
    except (json.JSONDecodeError, KeyError):
        return Response({'error': 'Invalid JSON or missing item_name parameter'}, status=status.HTTP_400_BAD_REQUEST)
    if item_name:
        # Example usage
        categories, sub_categories, other_keywords = generate_keywords(item_name)

        print("Categories:", categories)
        print("Sub-Categories:", sub_categories)
        print("Other Keywords:", other_keywords)
        customer=Customer.objects.filter(id=user_id).get()
        if len(categories)>1:
            customerCategory=CustomerCategory.objects.filter(customer=customer,category=categories[0],sub_category=categories[1])
            if customerCategory.exists():
                customerCategory.update(clicks=customerCategory.get().clicks+1,score=customerCategory.get().score+1)
            else :
                customerCategory_obj=CustomerCategory.objects.create(customer=customer,category=categories[0],sub_category=categories[1],clicks=1,score=1)
        else:
            customerCategory=CustomerCategory.objects.filter(customer=customer,category=categories[0],sub_category=sub_categories[0] if len(sub_categories)>0 else "" )
            if customerCategory.exists():
                    customerCategory.update(clicks=customerCategory.get().clicks+1,score=customerCategory.get().score+1)
            else :
                customerCategory=CustomerCategory.objects.create(customer=customer,category=categories[0],sub_category=sub_categories[0] if len(sub_categories)>0 else "" ,clicks=1,score=1)
        print(other_keywords)
        for kw in other_keywords:
            print(kw)
            if len(categories)>1:
                customerCategory=CustomerCategory.objects.filter(customer=customer,category=categories[0],sub_category=categories[1]).first()
            else:
                customerCategory=CustomerCategory.objects.filter(customer=customer,category=categories[0],sub_category=sub_categories[0] if len(sub_categories)>0 else "" ).first()
            customer_category_keyword=CustomerCategoryKeyword.objects.filter(customer=customer,customer_category=customerCategory,keyword=kw if len(kw)>0 else "")
            if customer_category_keyword.exists():
                    customer_category_keyword.update(clicks=customer_category_keyword.get().clicks+1,score=customer_category_keyword.get().score+1)
            else :
                print("customerCategory")
                customer_category_keyword=CustomerCategoryKeyword.objects.create(customer=customer,customer_category=customerCategory,keyword=kw if len(kw)>0 else "" ,clicks=1,score=1,searches=0)
                    

        return Response({"success": 1}, status=status.HTTP_200_OK)
                
    else:
        return Response({'error': 'url parameter is required'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_by_name(request):
    
    try:
        item_names =request.query_params.getlist('item_name') 
        user_id = int(request.GET.get('user_id'))
    except (json.JSONDecodeError, KeyError):
        return Response({'error': 'Invalid JSON or missing item_name parameter'}, status=status.HTTP_400_BAD_REQUEST)
    if len(item_names)>0:
        # Example usage
        print (item_names)
        # # item_temp_obj=[{
        # #     "item_name": "foo",
        # #     "score":10,
        # # }]
        # customer=Customer.objects.filter(id=user_id).get()
        # item_temp_obj_list=[]
        # for item_name in item_names:
        #     print (item_name)
        #     categories, sub_categories, other_keywords = generate_keywords(item_name)

        #     print("Categories:", categories)
        #     print("Sub-Categories:", sub_categories)
        #     print("Other Keywords:", other_keywords)

        #     item_temp_obj={
        #             "item_name": item_name,
        #             "score":0,
        #         }
        #     print (categories[0].strip().replace(","," "))
        #     try:
        #         if len(categories)>1:
        #             category=categories[0].replace(","," ").strip()
        #             sub_category=categories[1].replace(","," ").strip()
        #             # customerCategory=CustomerCategory.objects.filter(customer=customer,category=categories[0].strip().replace(","," "),sub_category=categories[1].strip().replace(","," ")).first()
        #             # print (categories[1].strip().replace(","," "))
        #         else:
        #             # customerCategory=CustomerCategory.objects.filter(customer=customer,category=categories[0].strip().replace(","," "),sub_category=sub_categories[0].strip().replace(","," ") if len(sub_categories)>0 else "" ).first()
        #             print ()
        #             category=categories[0].replace(","," ").strip()
        #             if len(sub_categories)>1:
        #                 sub_category=sub_categories[0].replace(","," ").strip()
        #             else:
        #                 sub_category=""
        #             # print (sub_categories[0].strip().replace(","," "))
        #         customerCategory=CustomerCategory.objects.filter(customer=customer,category=category,sub_category=sub_category if len(sub_categories)>0 else "" ).first()
        #         if customerCategory is None:
        #             customerCategory=CustomerCategory.objects.filter(customer=customer,category=categories[0].strip().replace(","," ")).first()
        #             if customerCategory is None: item_temp_obj['score'] = 0
        #             else:item_temp_obj['score'] = item_temp_obj['score']+int(customerCategory.score/2)
        #         else:
        #             item_temp_obj['score'] = item_temp_obj['score']+int(customerCategory.score)
        #     except Exception as e:
        #             item_temp_obj['score'] = 0

          
        #     # item_temp_obj['score'] = item_temp_obj['score']+customerCategory.score

        #     customer_category_keywords=CustomerCategoryKeyword.objects.filter(customer=customer,keyword__in=other_keywords if len(other_keywords)>0 else [])
        #     for customer_category_keyword in customer_category_keywords:
        #         item_temp_obj['score'] = item_temp_obj['score']+int(customer_category_keyword.score)
        #     print (item_temp_obj)
        #     item_temp_obj_list.append(item_temp_obj)
        
        #     # Sort items by score in descending order
        
        # sorted_items = sorted(item_temp_obj_list, key=lambda x: x['score'], reverse=True)
        # print (sorted_items)
        # item_names = [item['item_name'] for item in sorted_items]
        return Response({"success": 1,"item_names":item_names}, status=status.HTTP_200_OK)
                
    else:
        return Response({'error': 'url parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
