from rest_framework import viewsets
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer
from teachers.permissions import ReadOnly


class TeacherViewSet(viewsets.ModelViewSet):

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (ReadOnly,)
