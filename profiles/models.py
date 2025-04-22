from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    child_count = models.PositiveIntegerField(default=0)
    youngest_child_age = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Age in months of the youngest child"
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        help_text="City, state or zip for local content"
    )
    # any other parent-specific preferences can be added here
