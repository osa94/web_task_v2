from django.db import models
from teachers.models import Teacher
from exams.models import Exam


class Task(models.Model):
    content = models.CharField(max_length=500, default='')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='tasks', default='')
    max_points = models.FloatField()
    owner = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='tasks', default='')

    def __str__(self):
        return f"Exam:{self.exam.title}     Owner:{self.owner.username}     Content:{self.content}"

