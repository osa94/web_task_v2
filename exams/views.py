from rest_framework import viewsets
from rest_framework import permissions
from exams.models import Exam
from teachers.models import Teacher
from students.models import Student
from exams.serializers import ExamSerializer
from exams.permissions import IsTeacherAndOwner


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (permissions.IsAuthenticated, IsTeacherAndOwner, )

    def get_current_teacher(self):
        teacher = Teacher.objects.get(username=self.request.user)
        return teacher

    def filter_queryset(self, queryset):
        return Exam.objects.filter(owner=self.get_current_teacher())

    def exam_already_exists(self):
        my_exam_titles = []

        for exam in self.filter_queryset(ExamViewSet.queryset):
            my_exam_titles.append(exam.title)

        if self.request.data['title'] in my_exam_titles:
            return True
        else:
            return False

    def perform_create(self, serializer):
        students = Student.objects.filter(teachers=self.get_current_teacher())

        if not self.exam_already_exists():
            return serializer.save(owner=self.get_current_teacher(), for_who=students)
        else:
            return self.permission_denied(self.request,
                                          message=f"Exam {self.request.data['title']} already exists")
