from django.urls import path
from django.urls import include
from rest_framework import routers
from exams.views import ExamViewSet


router = routers.DefaultRouter()
router.register('', ExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
