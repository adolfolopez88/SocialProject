from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):
	return render(request, 'userprofiles/home.html', {})




