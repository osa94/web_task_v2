from django.db import models
from tasks.models import Task
from students.models import Student


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, default='', related_name='answers')
    answer = models.TextField(blank=True, default='')
    owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='answers', default='')

    def __str__(self):
        return f"Owner:{self.owner.username.username}      Task:{self.task.content}     Answer:{self.answer}"



