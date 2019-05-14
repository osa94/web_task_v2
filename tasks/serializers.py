from rest_framework import serializers
from exams.models import Exam
from tasks.models import Task
from teachers.models import Teacher


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    answers = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username.username')
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())

    def __init__(self, *args, **kwargs):
        super(TaskSerializer, self).__init__(*args, **kwargs)
        current_user = self.context['request'].user
        teacher = Teacher.objects.get(username=current_user)
        self.fields['exam'].queryset = Exam.objects.filter(owner=teacher)

    class Meta:
        model = Task
        fields = ('id', 'owner',  'exam', 'content', 'answers', 'max_points', )
