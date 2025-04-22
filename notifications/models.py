from django.conf import settings
from django.db import models


class Notification(models.Model):
    NOTIF_TYPES = [
        ('NEW_ANSWER', 'New Answer'),
        ('MENTION', 'Mention'),
        # Add more notification types as needed
    ]
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPES)
    payload = models.JSONField(
        help_text="Dynamic data for the notification, e.g., question ID, answer ID, etc."
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', 'is_read']),
        ]
