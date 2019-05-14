from django.urls import path
from django.urls import include
from rest_framework import routers
from tasks.views import TaskViewSet


router = routers.DefaultRouter()
router.register('', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
