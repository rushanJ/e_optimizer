from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    search_intrest_string = models.TextField(default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class CustomerCategory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    clicks = models.IntegerField()
    searches = models.IntegerField(default=1)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.customer} - {self.category} - {self.sub_category}"
    
class CustomerCategoryKeyword(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,default=1)
    customer_category = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    clicks = models.IntegerField()
    searches = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.customer_category} - {self.keyword}"