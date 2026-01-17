from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from .models import *
from history.models import HistoryUserApp


@receiver(signal=post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('Created')


@receiver(signal=pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    HistoryUserApp.objects.create(
        profile=instance,
        is_status='denied'
    )
