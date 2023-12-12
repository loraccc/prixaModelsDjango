from django.contrib import admin

from .models import Student,Course,Lesson
# Register your models here.

class OfficerAdmin(admin.ModelAdmin):
    list_display = ('officer_id', 'name', 'department', 'salary')
    list_filter = ('department',)
    search_fields = ('name',)

admin.site.site_header = 'Officers'
# admin.site.register(Officer, OfficerAdmin)

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Lesson)