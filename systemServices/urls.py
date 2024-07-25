from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SystemServiceViewSet, search_by_url_pattern,get_user_preference,order_by_name

router = DefaultRouter()
router.register(r'system_services', SystemServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search_by_url_pattern/', search_by_url_pattern, name='search_by_url_pattern'),  # Custom API endpoint
    path('get_user_preference/', get_user_preference, name='get_user_preference'),  # Custom API endpoint
    path('order_by_name/', order_by_name, name='order_by_name'),  # Custom API endpoint

]
