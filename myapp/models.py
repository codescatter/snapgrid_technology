from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    website = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    
    
class Query(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    website = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    
class About(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    website = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
    
    
class Home_Service(models.Model):
    icon = models.ImageField()
    heading = models.CharField(max_length=500)
    description = models.CharField(max_length=50000)
    
class Logo(models.Model):
    main_logo = models.ImageField()
    hover_logo = models.ImageField()
    
class Php_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
    
class android_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
    
class ml_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
    
class python_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
    
class django_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
    
class ai_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
class java_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
class ds_intern(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=5000)
    address = models.CharField(max_length=5000)
    
