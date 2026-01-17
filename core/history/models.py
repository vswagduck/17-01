from django.db import models
from rest_framework.authentication import get_user_model
User = get_user_model()

# Create your models here.
class HistoryUserApp(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT
    )
    is_status = models.CharField(
        choices=[
            ('active', 'active'),
            ('moderation', 'moderation'),
            ('denied', 'denied'),
])
    created = models.DateTimeField(auto_now_add=True)
