from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the current user is the author of the object (question/answer)
        return obj.author == request.user
