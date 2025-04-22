from django.db import models

from django.conf import settings


class QuestionPostedEvent(models.Model):
    question = models.ForeignKey(
        'qna.Question',
        on_delete=models.CASCADE,
        related_name='posted_events'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    timestamp = models.DateTimeField()



class AnswerPostedEvent(models.Model):
    answer = models.ForeignKey(
        'qna.Answer',
        on_delete=models.CASCADE,
        related_name='posted_events'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    timestamp = models.DateTimeField()
