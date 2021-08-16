from django.urls import path

from . import views

urlpatterns = [
    path('studentList/', views.showStudents, )
]
