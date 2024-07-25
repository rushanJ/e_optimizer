# item_api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('get-aliexpress-item-name/', views.get_aliexpress_item_name_view, name='get_aliexpress_item_name'),
]
