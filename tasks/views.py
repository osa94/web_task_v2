from rest_framework import viewsets
from rest_framework import permissions
from tasks.models import Task
from teachers.models import Teacher
from exams.models import Exam
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_current_teacher(self):
        teacher = Teacher.objects.get(username=self.request.user)
        return teacher

    def get_current_exam(self):
        exam_id = self.request.data['exam']
        exam = Exam.objects.get(id=exam_id)
        return exam

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.get_current_teacher())

    def perform_create(self, serializer):
        return serializer.save(exam=self.get_current_exam(), owner=self.get_current_teacher())
