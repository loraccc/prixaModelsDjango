from django.contrib import admin
from django.urls import path,include
from . import views
from .views import StudentListView,StudentDetailView

# urls.py
urlpatterns = [
    path('students/', StudentListView.as_view(), name='students'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]
