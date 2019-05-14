from rest_framework import serializers
from final_grades.models import FinalGrade
from exams.models import Exam
from students.models import Student
from teachers.models import Teacher
from django.db.models import Q


class FinalGradeSerializer(serializers.HyperlinkedModelSerializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all())
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())

    @staticmethod
    def filter_by_students(teacher):
        my_students = teacher.students.all()
        filter_by_students = Q()
        for student in my_students:
            filter_by_students.add(Q(username=student.username), Q.OR)
        return filter_by_students

    def __init__(self, *args, **kwargs):
        super(FinalGradeSerializer, self).__init__(*args, **kwargs)
        current_user = self.context['request'].user
        try:
            teacher = Teacher.objects.get(username=current_user)
        except Teacher.DoesNotExist:
            pass
        else:
            self.fields['exam'].queryset = Exam.objects.filter(owner=teacher)
            self.fields['student'].queryset = Student.objects.filter(FinalGradeSerializer.filter_by_students(teacher))

    class Meta:
        model = FinalGrade
        fields = ('id', 'exam', 'student', 'final_grade', )
