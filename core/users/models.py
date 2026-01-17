from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255,blank=True, null=True)
    last_name = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.user.username
