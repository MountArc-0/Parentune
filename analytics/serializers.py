from rest_framework import serializers
from .models import QuestionPostedEvent, AnswerPostedEvent


class QuestionPostedEventSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='question.id', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = QuestionPostedEvent
        fields = ('id', 'question_id', 'user_id', 'timestamp')


class AnswerPostedEventSerializer(serializers.ModelSerializer):
    answer_id = serializers.IntegerField(source='answer.id', read_only=True)
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = AnswerPostedEvent
        fields = ('id', 'answer_id', 'user_id', 'timestamp')
