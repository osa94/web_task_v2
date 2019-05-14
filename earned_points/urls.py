from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import EarnedPointsViewSet


router = routers.DefaultRouter()
router.register('', EarnedPointsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
