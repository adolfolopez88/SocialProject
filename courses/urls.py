from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^courses/$', views.CourseListBySchool.as_view(), name='course_list'),
]