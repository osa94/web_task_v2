from rest_framework import serializers
from tasks.models import Task
from answers.models import Answer


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username.username')
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all(), )

    class Meta:
        model = Answer
        fields = ('id', 'owner', 'task', 'answer',)
