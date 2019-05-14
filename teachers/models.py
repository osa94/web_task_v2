from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.username.username
