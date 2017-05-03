from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^schools$', views.SchoolListApi.as_view(), name='school_list'),
]