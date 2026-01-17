from django.db import models
from rest_framework.authentication import  get_user_model

User = get_user_model()
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=128)
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description= models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.cart.owner.username


