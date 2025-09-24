from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='register_student'),   # default /students/
    path('register/', views.register_student, name='register_student'),
    path('list/', views.student_list, name='student_list'),
]
