from django.contrib import admin
from django.urls import path,include
from . import views
from .views import (
    StudentListView,Lessonlist,
                     StudentDetailView,
                    LessonDeleteView, 
                     LessonCreateView, LessonUpdateView, 
                     
                    )

urlpatterns = [

    #Students CRUd

    # path('students/', views.studentList, name='student_list'),
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),

    #Lessions Crud
    path('lessons/',views.Lessonlist, name='lesson_list'),
    # path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
]
