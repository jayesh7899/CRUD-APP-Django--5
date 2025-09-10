from django.contrib import admin

from .models import Student

# Register your models here.

admin.site.register(Student)
class StudAdmin(admin.ModelAdmin):
    list_display=('stud_id', 'name', 'email', 'contact')
