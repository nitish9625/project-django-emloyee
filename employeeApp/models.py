from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    isActive = [
        ('1',"user Active"),
        ('0', "user offline")
    ]
    empcode = models.CharField(max_length=20)
    empname = models.CharField(max_length=50)
    empemail = models.EmailField()
    empactive = models.CharField(max_length=2, choices=isActive)



