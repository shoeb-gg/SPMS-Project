from django.urls import path

from . import views

urlpatterns = [
    path('', views.showLogIn, name="logIn" ),
    path('/faculty/', views.showFaculty, name="faculty" ),
]
