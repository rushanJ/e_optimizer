from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, CustomerCategoryViewSet, CustomerCategoryKeywordViewSet,RegisterView, LoginView

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'customer_categories', CustomerCategoryViewSet)
router.register(r'customer_category_keywords', CustomerCategoryKeywordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
