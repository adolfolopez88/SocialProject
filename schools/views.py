from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import School

class SchoolList(ListView):
	model = School

#Rest Framework
from rest_framework import generics
from .serializers import SchoolSerializer

class SchoolListApi(generics.ListCreateAPIView):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(queryset, pk=self.kwargs['pk'],)
		return obj