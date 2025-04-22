from rest_framework import serializers


class FeedSerializer(serializers.Serializer):
    payload = serializers.ListField()
    generated_at = serializers.DateTimeField()
