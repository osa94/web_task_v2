from rest_framework import serializers
from exams.models import Exam
from tasks.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username.username')
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'owner',  'exam', 'content', 'max_points', )
