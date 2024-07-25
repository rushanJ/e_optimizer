from django.db import models

class SystemService(models.Model):
    service = models.CharField(max_length=100)
    url_pattern = models.CharField(max_length=255)
    page_type = models.CharField(max_length=50)
    title_css = models.CharField(max_length=255)
    list_attribute = models.CharField(max_length=255,default="li")
    list_css= models.CharField(max_length=255,default=None,null=True)
    list_attribute_value = models.CharField(max_length=255,default='null')
    item_title_query_selector = models.CharField(max_length=255,default='null')
    list_selector_type=models.CharField(max_length=255,default="ATTRIBUTE")
    items_to_drop=models.IntegerField(default=2)
    item_identification_id = models.CharField(max_length=255,default='id')

    action = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service} - {self.url_pattern}"
