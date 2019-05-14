from rest_framework import permissions
from teachers.models import Teacher


class ExamOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            teacher = Teacher.objects.get(username=request.user)
        except Teacher.DoesNotExist:
            return False
        else:
            return teacher.username == obj.owner.username

    def has_permission(self, request, view):
        try:
            Teacher.objects.get(username=request.user)
        except Teacher.DoesNotExist:
            return False
        else:
            return True




