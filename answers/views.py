from rest_framework import viewsets
from rest_framework import permissions
from answers.models import Answer
from teachers.models import Teacher
from students.models import Student
from tasks.models import Task
from django.db.models import Q
from answers.serializers import AnswerSerializer
from answers.permissions import OwnerCanSolveTeacherCanRead


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.IsAuthenticated, OwnerCanSolveTeacherCanRead, )

    def get_serializer_context(self):
        return {'request': self.request}

    def get_current_student(self):
        student = Student.objects.get(username=self.request.user)
        return student

    def get_current_teacher(self):
        teacher = Teacher.objects.get(username=self.request.user)
        return teacher

    @staticmethod
    def filter_by_tasks(my_tasks):
        filter_query = Q()
        for task in my_tasks:
            filter_query.add(Q(task=task), Q.OR)
        return filter_query

    def filter_queryset(self, queryset):
        try:
            teacher = self.get_current_teacher()
        except Teacher.DoesNotExist:
            student = self.get_current_student()
            return queryset.filter(owner=student)
        else:
            my_tasks = Task.objects.filter(owner=teacher)
            return queryset.filter(AnswerViewSet.filter_by_tasks(my_tasks))

    def task_is_already_solved(self):
        current_task_id = self.request.data['task']
        answers_to_this_task = Answer.objects.filter(task=current_task_id)
        current_student = self.get_current_student()
        all_who_answered = []

        for answer in answers_to_this_task:
            all_who_answered.append(answer.owner)

        if current_student in all_who_answered:
            return True
        else:
            return False

    def perform_create(self, serializer):
        if not self.task_is_already_solved():
            return serializer.save(owner=self.get_current_student())
        else:
            return self.permission_denied(self.request, message="You already solved this task")

