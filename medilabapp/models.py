from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()

class Register(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    medicalhistory = models.CharField(max_length=250)