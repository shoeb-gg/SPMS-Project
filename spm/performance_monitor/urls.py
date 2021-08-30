from django.urls import path

from . import views

urlpatterns = [
    path('', views.showLogIn, name="logIn" ),
    path('/faculty/', views.showFaculty, name="facultyDash" ),
    path('/faculty/Data/', views.showFacultyDataEntry, name="facultyData" ),
    path('/faculty/StudentReport/', views.showFacultyStudentReport, name="facultyStudentReport" ),
]
