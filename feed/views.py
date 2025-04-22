from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import FeedSerializer
from .models import CacheFeed


class FeedViewSet(viewsets.ModelViewSet):
    queryset = CacheFeed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Assuming you have a Feed model and a way to filter it
        return CacheFeed.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        cache_feed = self.get_queryset().first()
        if cache_feed:
            serializer = self.get_serializer(cache_feed)
            return Response(serializer.data)
        return Response({"detail": "Feed not generated yet."}, status=404)

    def create(self, request, *args, **kwargs):
        payload = request.data.get('payload')
        if not payload:
            return Response({"detail": "Payload is required."}, status=400)

        obj, _ = CacheFeed.objects.update_or_create(
            user=request.user,
            defaults={'payload': payload}
        )
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
