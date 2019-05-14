from rest_framework import viewsets
from final_grades.models import FinalGrade
from teachers.models import Teacher
from students.models import Student
from exams.models import Exam
from final_grades.serializers import FinalGradeSerializer
from rest_framework import permissions
from final_grades.permissions import ExamOwner


class FinalGradeViewSet(viewsets.ModelViewSet):
    queryset = FinalGrade.objects.all()
    serializer_class = FinalGradeSerializer
    permission_classes = (permissions.IsAuthenticated, ExamOwner)

    def get_serializer_context(self):
        return {'request': self.request}

    def get_logged_teacher(self):
        return Teacher.objects.get(username=self.request.user)

    def get_current_exam(self):
        current_exam_id = self.request.data['exam']
        current_exam = Exam.objects.get(id=current_exam_id)
        return current_exam

    def get_my_students(self):
        teacher = self.get_logged_teacher()
        my_students = teacher.students.all()
        return my_students

    def get_student_to_evaluate(self):
        student_id = self.request.data['student']
        student = Student.objects.get(id=student_id)
        return student

    def filter_queryset(self, queryset):
        return FinalGrade.objects.filter(owner=self.get_logged_teacher())

    def exam_already_checked(self):
        exam = self.get_current_exam()
        given_grades_for_current_exam = FinalGrade.objects.filter(exam=exam)
        noted_students = []

        for grade in given_grades_for_current_exam:
            noted_students.append(grade.student)
        if self.get_student_to_evaluate() in noted_students:
            return True
        else:
            return False

    def perform_create(self, serializer):
        if not self.exam_already_checked():
            return serializer.save(student=self.get_student_to_evaluate(),
                                   exam=self.get_current_exam(),
                                   owner=self.get_logged_teacher(),
                                   )
        else:
            return self.permission_denied(self.request, message="You already rated this student for this exam")


