from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import QuestionPostedEvent, AnswerPostedEvent
from .serializers import QuestionPostedEventSerializer, AnswerPostedEventSerializer


class QuestionPostedEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows question posted events to be viewed or edited.
    """
    queryset = QuestionPostedEvent.objects.all()
    serializer_class = QuestionPostedEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AnswerPostedEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows answer posted events to be viewed or edited.
    """
    queryset = AnswerPostedEvent.objects.all()
    serializer_class = AnswerPostedEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
