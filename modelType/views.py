from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import CommonInfo,Student
# Create your views here.


# def studentList(request):
#     students = Student.objects.all()
#     context = {
#         'students': students
#     }
#     return render(request, 'index.html',context)

class StudentListView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'students'