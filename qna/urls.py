from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerViewSet, TagViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='questions')
router.register(r'answers', AnswerViewSet, basename='answers')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = router.urls
