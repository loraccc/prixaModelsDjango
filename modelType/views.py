from django.shortcuts import render,get_object_or_404, redirect
from django.views import generic
from django.views.generic import ListView,DetailView
from .models import CommonInfo,Student
from django.urls import reverse_lazy
from django.views import View
from .models import Lesson
from .forms import LessonForm
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

class LessonListView(View):
    template_name = 'lesson_list.html'

    def get(self, request):
        lessons = Lesson.objects.all()
        return render(request, self.template_name, {'lessons': lessons})

class LessonCreateView(View):
    template_name = 'lesson_form.html'

    def get(self, request):
        form = LessonForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
        return render(request, self.template_name, {'form': form})

class LessonUpdateView(View):
    template_name = 'lesson_form.html'

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        form = LessonForm(instance=lesson)
        return render(request, self.template_name, {'form': form, 'lesson': lesson})

    def post(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
        return render(request, self.template_name, {'form': form, 'lesson': lesson})

class LessonDeleteView(View):
    template_name = 'lesson_confirm_delete.html'

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        return render(request, self.template_name, {'lesson': lesson})

    def post(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        lesson.delete()
        return redirect('lesson_list')
