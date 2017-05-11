from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CourseViewSet
from rest_framework import renderers

course_list = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
	url(r'^courses$', course_list, name='course_list'),
	url(r'^courses/(?P<pk>[0-9]+)/$', course_detail, name='course_detail'),
]