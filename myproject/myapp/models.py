from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return self.name




# Create your models here
# class Product(models.Model):
#     name = models.CharField(max_length=50,  blank= False),
#     # name = models.CharField(max_length=200, blank=True)
#     description= models.TextField(),

#     def __str__(self):
#         return self.name

