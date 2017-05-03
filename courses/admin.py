from django.contrib import admin
from .models import Course

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
	list_display = ('name', )
	