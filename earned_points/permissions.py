from rest_framework import permissions
from teachers.models import Teacher


class IsTeacherAndGivesPoints(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.method == "DELETE":
            return obj.who_gives_points.username == request.user
        else:
            return False

    def has_permission(self, request, view):
        try:
            Teacher.objects.get(username=request.user)
        except Teacher.DoesNotExist:
            return False
        else:
            return True
