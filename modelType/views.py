from django.shortcuts import render
from django.views import generic
from .models import CommonInfo,Student
# Create your views here.


def studentList(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html',context)