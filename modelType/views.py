from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView,DetailView
from .models import CommonInfo,Student
from django.urls import reverse_lazy
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


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'  # Create this template

    def get_success_url(self):
        return reverse_lazy('student_list')