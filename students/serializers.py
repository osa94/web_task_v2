from rest_framework import serializers
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username', )
    teachers = serializers.StringRelatedField(many=True, read_only=True)
    exams = serializers.StringRelatedField(many=True, read_only=True)
    answers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'username', 'teachers', 'exams', 'answers',)
