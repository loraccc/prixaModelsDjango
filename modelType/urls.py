from django.contrib import admin
from django.urls import path,include
from . import views
from .views import StudentListView

urlpatterns = [
    path('students/',views.StudentListView.as_view(),name='students')
]
