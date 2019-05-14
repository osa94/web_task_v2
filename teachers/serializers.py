from rest_framework import serializers
from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')

    class Meta:
        model = Teacher
        fields = ('id', 'username',)
