from django.db import models
from accounts.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Restaurant, related_name='locations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    location = models.ForeignKey(Location, related_name='menus', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    menu = models.ForeignKey(Menu, related_name='categories', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
