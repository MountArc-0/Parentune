from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get', 'patch'], url_path='me')
    def me(self, request):
        try:
            profile, _ = UserProfile.objects.get_or_create(user=request.user)
            if request.method == 'PATCH':
                serializer = self.get_serializer(profile, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
            if request.method == 'GET':
                serializer = self.get_serializer(profile)
                return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response(status=404)
