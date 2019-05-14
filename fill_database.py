import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
django.setup()

from django.contrib.auth.models import User
from teachers.models import Teacher
from students.models import Student
from exams.models import Exam
from tasks.models import Task
from answers.models import Answer
from earned_points.models import EarnedPoints
from final_grades.models import FinalGrade

"""  admin """
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

""" teachers """
TEACHER1_USERNAME = 'Teacher1'
TEACHER2_USERNAME = 'Teacher2'

""" students """
STUDENT1_USERNAME = 'Student1'
STUDENT2_USERNAME = 'Student2'
STUDENT3_USERNAME = 'Student3'

"""password for teachers and students"""
PASSWORD = 'TypicalCommonUser'

""" exams """
TEACHER1_EXAM_TITLE = 'Addition'
TEACHER2_EXAM_TITLE = 'Division'

""" tasks """
ADDITION_EXAM_CONTENT1 = "How much is 2 + 2?"
ADDITION_EXAM_CONTENT2 = "How much is 3 + 3?"
ADDITION_EXAM_MAX_POINTS1 = 1.0
ADDITION_EXAM_MAX_POINTS2 = 2.0

DIVISION_EXAM_CONTENT1 = "How much is 2 / 2?"
DIVISION_EXAM_CONTENT2 = "How much is 6 / 2?"
DIVISION_EXAM_MAX_POINTS1 = 1.0
DIVISION_EXAM_MAX_POINTS2 = 2.0

""" answers """
ADDITION_STUDENT1_TASK1 = '4'
ADDITION_STUDENT1_TASK2 = '6'
ADDITION_STUDENT2_TASK1 = '4'
ADDITION_STUDENT2_TASK2 = '6'

DIVISION_STUDENT2_TASK1 = '1'
DIVISION_STUDENT2_TASK2 = '2'
DIVISION_STUDENT3_TASK1 = '1'
DIVISION_STUDENT3_TASK2 = '2'

""" earned points """
ADDITION_STUDENT1_TASK1_EARNED = 1.0
ADDITION_STUDENT1_TASK2_EARNED = 2.0
ADDITION_STUDENT2_TASK1_EARNED = 1.0
ADDITION_STUDENT2_TASK2_EARNED = 2.0

DIVISION_STUDENT2_TASK1_EARNED = 1.0
DIVISION_STUDENT2_TASK2_EARNED = 2.0
DIVISION_STUDENT3_TASK1_EARNED = 1.0
DIVISION_STUDENT3_TASK2_EARNED = 2.0

""" final grades """
GRADE = 5.0

""" create admin """
User.objects.create_user(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, is_superuser=True, is_staff=True, )

""" create teachers """
user = User.objects.create_user(username=TEACHER1_USERNAME, password=PASSWORD, )
user.save()
Teacher1 = Teacher.objects.create(username=user)

user = User.objects.create_user(username=TEACHER2_USERNAME, password=PASSWORD, )
user.save()
Teacher2 = Teacher.objects.create(username=user)

""" create students """
user = User.objects.create_user(username=STUDENT1_USERNAME, password=PASSWORD, )
user.save()
Student1 = Student.objects.create(username=user)
Student1.teachers.set((Teacher1,))

user = User.objects.create_user(username=STUDENT2_USERNAME, password=PASSWORD, )
user.save()
Student2 = Student.objects.create(username=user)
Student2.teachers.set((Teacher1, Teacher2,))

user = User.objects.create_user(username=STUDENT3_USERNAME, password=PASSWORD, )
user.save()
Student3 = Student.objects.create(username=user)
Student3.teachers.set((Teacher2,))

""" create exams """
exam_Addition = Exam.objects.create(title=TEACHER1_EXAM_TITLE, owner=Teacher1)
exam_Addition.for_who.set((Student1, Student2,))

exam_Division = Exam.objects.create(title=TEACHER2_EXAM_TITLE, owner=Teacher2)
exam_Division.for_who.set((Student2, Student3,))

""" create tasks """
task1_Addition = Task.objects.create(content=ADDITION_EXAM_CONTENT1,
                                     exam=exam_Addition,
                                     max_points=ADDITION_EXAM_MAX_POINTS1,
                                     owner=Teacher1,
                                     )

task2_Addition = Task.objects.create(content=ADDITION_EXAM_CONTENT2,
                                     exam=exam_Addition,
                                     max_points=ADDITION_EXAM_MAX_POINTS2,
                                     owner=Teacher1,
                                     )

task1_Division = Task.objects.create(content=DIVISION_EXAM_CONTENT1,
                                     exam=exam_Division,
                                     max_points=DIVISION_EXAM_MAX_POINTS1,
                                     owner=Teacher2,
                                     )

task2_Division = Task.objects.create(content=DIVISION_EXAM_CONTENT2,
                                     exam=exam_Division,
                                     max_points=DIVISION_EXAM_MAX_POINTS2,
                                     owner=Teacher2,
                                     )

""" create answers """
answer1_Student1_Addition = Answer.objects.create(task=task1_Addition, answer=ADDITION_STUDENT1_TASK1, owner=Student1)
answer2_Student1_Addition = Answer.objects.create(task=task2_Addition, answer=ADDITION_STUDENT1_TASK2, owner=Student1)
answer1_Student2_Addition = Answer.objects.create(task=task1_Addition, answer=ADDITION_STUDENT2_TASK1, owner=Student2)
answer2_Student2_Addition = Answer.objects.create(task=task2_Addition, answer=ADDITION_STUDENT2_TASK2, owner=Student2)

answer1_Student2_Division = Answer.objects.create(task=task1_Division, answer=DIVISION_STUDENT2_TASK1, owner=Student2)
answer2_Student2_Division = Answer.objects.create(task=task2_Division, answer=DIVISION_STUDENT2_TASK2, owner=Student2)
answer1_Student3_Division = Answer.objects.create(task=task1_Division, answer=DIVISION_STUDENT3_TASK1, owner=Student3)
answer2_Student3_Division = Answer.objects.create(task=task2_Division, answer=DIVISION_STUDENT3_TASK2, owner=Student3)

""" create earned points """
EarnedPoints.objects.create(answer=answer1_Student1_Addition,
                            earned_points=ADDITION_STUDENT1_TASK1_EARNED,
                            who_gives_points=Teacher1)

EarnedPoints.objects.create(answer=answer2_Student1_Addition,
                            earned_points=ADDITION_STUDENT1_TASK2_EARNED,
                            who_gives_points=Teacher1)

EarnedPoints.objects.create(answer=answer1_Student2_Addition,
                            earned_points=ADDITION_STUDENT2_TASK1_EARNED,
                            who_gives_points=Teacher1)

EarnedPoints.objects.create(answer=answer2_Student2_Addition,
                            earned_points=ADDITION_STUDENT2_TASK2_EARNED,
                            who_gives_points=Teacher1)

EarnedPoints.objects.create(answer=answer1_Student2_Division,
                            earned_points=DIVISION_STUDENT2_TASK1_EARNED,
                            who_gives_points=Teacher2)

EarnedPoints.objects.create(answer=answer2_Student2_Division,
                            earned_points=DIVISION_STUDENT2_TASK2_EARNED,
                            who_gives_points=Teacher2)

EarnedPoints.objects.create(answer=answer1_Student3_Division,
                            earned_points=DIVISION_STUDENT3_TASK1_EARNED,
                            who_gives_points=Teacher2)

EarnedPoints.objects.create(answer=answer2_Student3_Division,
                            earned_points=DIVISION_STUDENT3_TASK2_EARNED,
                            who_gives_points=Teacher2)

""" create final grades """
FinalGrade.objects.create(exam=exam_Addition,
                          student=Student1,
                          final_grade=GRADE,
                          owner=Teacher1,
                          )

FinalGrade.objects.create(exam=exam_Addition,
                          student=Student2,
                          final_grade=GRADE,
                          owner=Teacher1,
                          )

FinalGrade.objects.create(exam=exam_Division,
                          student=Student2,
                          final_grade=GRADE,
                          owner=Teacher2,
                          )

FinalGrade.objects.create(exam=exam_Division,
                          student=Student3,
                          final_grade=GRADE,
                          owner=Teacher2,
                          )
exit()
