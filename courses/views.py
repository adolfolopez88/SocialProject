from django.shortcuts import render
from django.views.generic import ListView
from .models import Course 

class CourseListBySchool(ListView):
	model = Course

	def get_queryset(self):
		school_id = self.request.GET.get('school')
		context = Course.objects.filter(school=school_id)	
		return context

#Rest Framework
from rest_framework import generics
from .serializers import CourseSerializer
from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer