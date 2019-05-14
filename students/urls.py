from django.urls import path
from django.urls import include
from rest_framework import routers
from students.views import StudentViewSet


router = routers.DefaultRouter()
router.register('', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
