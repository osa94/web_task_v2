from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import FinalGradeViewSet


router = routers.DefaultRouter()
router.register('', FinalGradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
