from rest_framework import serializers
from tasks.models import Task
from .models import Answer
from students.models import Student
from django.db.models import Q


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    earned_points = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username.username')
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), )

    @staticmethod
    def filter_by_teacher(student):
        my_teachers = student.teachers.all()
        filter_by_teachers = Q()
        for teacher in my_teachers:
            filter_by_teachers.add(Q(owner=teacher), Q.OR)
        return filter_by_teachers

    def __init__(self, *args, **kwargs):
        super(AnswerSerializer, self).__init__(*args, **kwargs)
        current_user = self.context['request'].user
        try:
            student = Student.objects.get(username=current_user)
        except Student.DoesNotExist:
            pass
        else:
            self.fields['task'].queryset = Task.objects.filter(AnswerSerializer.filter_by_teacher(student))

    class Meta:
        model = Answer
        fields = ('id', 'owner', 'task', 'answer', 'earned_points',)
