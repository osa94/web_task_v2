from django.db import models
from teachers.models import Teacher
from students.models import Student


class Exam(models.Model):
    title = models.CharField(max_length=200, default='')
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='exams')
    for_who = models.ManyToManyField(Student, related_name='exams')

    def __str__(self):
        return f"Exam:{self.title}   Teacher:{self.owner.username.username}"
