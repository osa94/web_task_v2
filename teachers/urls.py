from django.urls import path
from django.urls import include
from rest_framework import routers
from teachers.views import TeacherViewSet


router = routers.DefaultRouter()
router.register('', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
