from rest_framework import viewsets
from students.models import Student
from students.serializers import StudentSerializer
from students.permissions import ReadOnly


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (ReadOnly, )
