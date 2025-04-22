from rest_framework.routers import DefaultRouter
from .views import QuestionPostedEventViewSet, AnswerPostedEventViewSet

router = DefaultRouter()
router.register(r'question-posted', QuestionPostedEventViewSet, basename='question-posted')
router.register(r'answer-posted', AnswerPostedEventViewSet, basename='answer-posted')

urlpatterns = router.urls
