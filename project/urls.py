from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('exams/', include('exams.urls')),
    path('tasks/', include('tasks.urls')),
    path('answers/', include('answers.urls')),
    path('earned_points/', include('earned_points.urls')),
    path('final_grades/', include('final_grades.urls')),
]
