from rest_framework import permissions
from teachers.models import Teacher
from students.models import Student


class OwnerCanSolveTeacherCanRead(permissions.BasePermission):

    @staticmethod
    def task_is_associated_with_teacher(request, obj, teacher):
        if (request.method in permissions.SAFE_METHODS) and (teacher == obj.task.owner):
            return True
        else:
            return False

    @staticmethod
    def is_teacher(request, obj):
        try:
            teacher = Teacher.objects.get(username=request.user)
        except Teacher.DoesNotExist:
            return False
        else:
            return OwnerCanSolveTeacherCanRead.task_is_associated_with_teacher(request, obj, teacher)

    def has_object_permission(self, request, view, obj):
        try:
            student = Student.objects.get(username=request.user)
        except Student.DoesNotExist:
            return OwnerCanSolveTeacherCanRead.is_teacher(request, obj)
        else:
            if (student.username == obj.owner.username) and (request.method in permissions.SAFE_METHODS):
                return True
            else:
                return False

    def has_permission(self, request, view):
        try:
            Student.objects.get(username=request.user)
        except Student.DoesNotExist:
            try:
                Teacher.objects.get(username=request.user)
            except Teacher.DoesNotExist:
                return False
            else:
                if request.method in permissions.SAFE_METHODS:
                    return True
                return False
        else:
            return True
