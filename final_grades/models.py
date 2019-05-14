from django.db import models
from exams.models import Exam
from students.models import Student
from teachers.models import Teacher


class FinalGrade(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='final_grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default='', related_name='final_grades')
    final_grade = models.FloatField(default='')
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='final_grades', default='')

    def __str__(self):
        return f"teacher:{self.owner}   student:{self.student.username}  exam:{self.exam.title}   " \
            f"final_grade:{self.final_grade}"
