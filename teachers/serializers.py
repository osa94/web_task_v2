from rest_framework import serializers
from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    students = serializers.StringRelatedField(many=True, read_only=True)
    exams = serializers.StringRelatedField(many=True, read_only=True)
    tasks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ('id', 'username', 'students', 'exams', 'tasks',)
