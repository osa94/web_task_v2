from django.db import models
from answers.models import Answer
from teachers.models import Teacher


class EarnedPoints(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default='', related_name='earned_points')
    earned_points = models.FloatField(blank=True, default='')
    who_gives_points = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='checked_answers')

    def __str__(self):
        return f"Task:{self.answer.task.content}     Answer:{self.answer.answer}"\
            f"      Earned/Max : {self.earned_points}/{self.answer.task.max_points}"\
            f"      who_answer:{self.answer.owner}"
