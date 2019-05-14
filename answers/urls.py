from django.urls import path
from django.urls import include
from rest_framework import routers
from answers.views import AnswerViewSet


router = routers.DefaultRouter()
router.register('', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
