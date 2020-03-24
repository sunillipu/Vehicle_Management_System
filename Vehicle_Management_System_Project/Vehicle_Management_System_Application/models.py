from django.db import models

# Create your models here.
class Super_Admin_Data(models.Model):
    name=models.CharField(max_length=50,null=True)
    super_admin_user_name=models.CharField(max_length=30)
    super_admin_password=models.CharField(max_length=20)
class Vehicle_Details(models.Model):
    vehicle_number=models.CharField(max_length=20)
    vehicle_type=models.CharField(max_length=30)
    vehicle_model=models.CharField(max_length=30)
    vehicle_description=models.TextField(max_length=300)
class Admin_Data(models.Model):
    name=models.CharField(max_length=50,null=True)
    admin_user_name=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=20)
class User_Data(models.Model):
    name=models.CharField(max_length=50)
    user_name=models.CharField(max_length=30)
    user_password=models.CharField(max_length=20)
