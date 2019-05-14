from rest_framework import viewsets
from rest_framework import permissions
from .models import EarnedPoints
from teachers.models import Teacher
from answers.models import Answer
from .serializers import EarnedPointsSerializer
from .permissions import IsTeacherAndGivesPoints


class EarnedPointsViewSet(viewsets.ModelViewSet):
    queryset = EarnedPoints.objects.all()
    serializer_class = EarnedPointsSerializer
    permission_classes = (permissions.IsAuthenticated, IsTeacherAndGivesPoints, )

    def get_serializer_context(self):
        return {'request': self.request}

    def get_current_answer(self):
        answer_id = self.request.data['answer']
        answer = Answer.objects.get(id=answer_id)
        return answer

    def get_current_teacher(self):
        return Teacher.objects.get(username=self.request.user)

    def answer_has_points(self):
        current_answer = self.get_current_answer()
        given_points = self.filter_queryset(EarnedPointsViewSet.queryset)
        answers = []
        for points in given_points:
            answers.append(points.answer)
        if current_answer in answers:
            return True
        else:
            return False

    def filter_queryset(self, queryset):
        teacher = self.get_current_teacher()
        return queryset.filter(who_gives_points=teacher)

    def perform_create(self, serializer):
        answer = self.get_current_answer()
        teacher = self.get_current_teacher()
        if not self.answer_has_points():
            return serializer.save(answer=answer, who_gives_points=teacher)
        else:
            return self.permission_denied(self.request, "You already checked this answer")
