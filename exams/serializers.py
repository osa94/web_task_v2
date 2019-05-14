from rest_framework import serializers
from exams.models import Exam


class ExamSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username.username')
    for_who = serializers.StringRelatedField(read_only=True, many=True)
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ('id', 'owner', 'title', 'tasks', 'for_who', )
