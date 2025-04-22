from django.conf import settings
from django.db import models


class CacheFeed(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    payload = models.JSONField()
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['generated_at']),
        ]
