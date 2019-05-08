from django.db import models

# Create your models here.

class Registration(models.Model):
    
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True, max_length=254)
    password = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

