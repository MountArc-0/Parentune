from rest_framework import serializers
from .models import Tag, Question, Answer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Answer
        fields = ['id', 'body', 'author', 'question', 'created_at', 'updated_at']


class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagSerializer(many=True, required=False)
    answers = AnswerSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'author', 'tags', 'answers', 'created_at']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        question = Question.objects.create(**validated_data)

        for tag in tags_data:
            obj, _ = Tag.objects.get_or_create(name=tag['name'], slug=tag['slug'])
            question.tags.add(obj)

        return question
