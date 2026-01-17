from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Cart, CartItem, Product, Category
from rest_framework.authentication import get_user_model

# User=get_user_model()


@receiver(post_save, sender=get_user_model())
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(owner=instance)
        print('Created cart')

