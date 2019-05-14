from rest_framework import serializers
from answers.models import Answer
from teachers.models import Teacher
from students.models import Student
from tasks.models import Task
from .models import EarnedPoints
from django.db.models import Q


class EarnedPointsSerializer(serializers.HyperlinkedModelSerializer):
    answer = serializers.PrimaryKeyRelatedField(queryset=Answer.objects.all())
    who_gives_points = serializers.StringRelatedField(read_only=True)

    @staticmethod
    def filter_by_students(teacher):
        my_students = Student.objects.filter(teachers=teacher)
        filter_by_students = Q()
        for student in my_students:
            filter_by_students.add(Q(owner=student), Q.OR)
        return filter_by_students

    @staticmethod
    def filter_by_tasks(teacher):
        my_tasks = Task.objects.filter(owner=teacher)
        filter_by_tasks = Q()
        for task in my_tasks:
            filter_by_tasks.add(Q(task=task), Q.OR)
        return filter_by_tasks

    def __init__(self, *args, **kwargs):
        super(EarnedPointsSerializer, self).__init__(*args, **kwargs)
        current_user = self.context['request'].user
        try:
            teacher = Teacher.objects.get(username=current_user)
        except Teacher.DoesNotExist:
            pass
        else:
            self.fields['answer'].queryset = Answer.objects.filter(EarnedPointsSerializer.filter_by_students(teacher),
                                                                   EarnedPointsSerializer.filter_by_tasks(teacher))

    class Meta:
        model = EarnedPoints
        fields = ('id', 'answer', 'earned_points', 'who_gives_points')
