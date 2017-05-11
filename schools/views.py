from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import School

class SchoolList(ListView):
	model = School

class SchoolDetail(DetailView):
	model = School

from rest_framework import generics
from .serializers import SchoolSerializer
from rest_framework import viewsets

class SchoolViewSet(viewsets.ModelViewSet):
	queryset = School.objects.all()
	serializer_class = SchoolSerializer

    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)
