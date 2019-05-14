from rest_framework import permissions
from teachers.models import Teacher


class IsTeacherAndOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            teacher = Teacher.objects.get(username=request.user)
        except Teacher.DoesNotExist:
            return False
        else:
            if request.method in permissions.SAFE_METHODS:
                return teacher == obj.owner
            else:
                return False

    def has_permission(self, request, view):
        try:
            Teacher.objects.get(username=request.user)
        except Teacher.DoesNotExist:
            return False
        else:
            return True
