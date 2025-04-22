from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username, email, password, first_name, last_name are already included in AbstractUser
    favorite_tags = models.ManyToManyField(
        'qna.Tag',
        blank=True,
        help_text="Parents' favorite topics for feed personalization.",
    )
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
