from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=40)
    Contact=models.BigIntegerField()
    Email=models.EmailField()
    Department=models.CharField(max_length=20)
    Code=models.CharField(max_length=20) 
    Image=models.ImageField(upload_to='image',null=True)
    

class Department(models.Model):
    Dep_name = models.CharField(max_length=100)
    Dep_code = models.CharField(max_length=20, unique=True)
    Dep_head = models.CharField(max_length=100)
    Dep_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Empquery(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField()
    Department=models.CharField(max_length=30)
    Query=models.TextField()
    Status=models.CharField(default="pending")
    Reply=models.TextField(null=True)

class Item(models.Model):
    Item_name=models.CharField(max_length=20)
    Item_desc=models.CharField(max_length=30)
    Item_price=models.IntegerField()
    Item_image=models.ImageField(upload_to='image',null=True)
    Item_color=models.CharField(max_length=20)
    Item_Qty=models.IntegerField()
    Item_category=models.CharField(max_length=20)


