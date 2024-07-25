from rest_framework import serializers
from .models import SystemService

class SystemServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemService
        fields = ['id', 'service', 'url_pattern', 'page_type', 'title_css', 'action','list_attribute','list_attribute_value','item_title_query_selector','list_selector_type','list_css','items_to_drop'
                  ,'item_identification_id' ]
