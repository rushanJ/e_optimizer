from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customer.urls')),
    path('api/item_api/', include('item_api.urls')),
    path('api/', include('systemServices.urls')),
]
