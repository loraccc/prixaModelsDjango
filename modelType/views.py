from typing import Any
from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView,DetailView
from .models import CommonInfo,Student
from django.urls import reverse_lazy
from django.views import View
from .models import Lesson,Course
from .forms import LessonForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
# Create your views here.


# def studentList(request):
#     students = Student.objects.all()
#     context = {
#         'students': students
#     }
#     for std in students:
#         print(std.name)
#     return render(request, 'index.html',context)

class StudentListView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'students'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = 'lorac'
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'  # Create this template

    def get_success_url(self):
        return reverse_lazy('student_list')


##############
#Lesson 
#############
# class LessonListView(View):
#     template_name = 'lesson_list.html'

#     def get(self, request):
#         lessons = Lesson.objects.all()
#         return render(request, self.template_name, {'lessons': lessons})

def Lessonlist(request):
    lessons = Lesson.objects.all().select_related('course')      
    # In select related we pass the key value that is set for foreign key . 
    for lesson in lessons:
        print(f"Lesson Title: {lesson.title},Course:{lesson.course.name}")
    context = {'lessons': lessons}
    return render(request, 'lesson_list.html',context)

#------------------USING SELECT RELATED--------------------
# def Lessonlist(request):
#     lessons = Lesson.objects.filter(course__name='DATA SCIENCE').select_related('course')      
#     # In select related we pass the key value that is set for foreign key . 
#     for lesson in lessons:
#         print(f"Lesson Title: {lesson.title},Course:{lesson.course.name}")
#     context = {'lessons': lessons}
#     return render(request, 'lesson_list.html',context)


class LessonCreateView(View):
    template_name = 'lesson_form.html'

    def get(self, request):
        form = LessonForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
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