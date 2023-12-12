from django.contrib import admin
from django.urls import path,include
from . import views
from .views import studentList

urlpatterns = [
    path('students/',views.studentList,name='students')
]
