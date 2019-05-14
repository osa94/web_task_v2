from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher


class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default='', )
    teachers = models.ManyToManyField(Teacher, related_name='students', )

    def __str__(self):
        return self.username.username

