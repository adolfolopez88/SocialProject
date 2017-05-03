from django.contrib import admin
from .models import School

@admin.register(School)
class AdminSchool(admin.ModelAdmin):
	list_display = ('name', )
