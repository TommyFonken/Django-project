from django.db import models

# Create your models here.
class UserChoice(models.Model):
    """models"""
    option = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    hostname = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
