from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SchoolViewSet
from rest_framework import renderers

school_list = SchoolViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

school_detail = SchoolViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
	url(r'^schools$', school_list, name='school_list'),
	url(r'^schools/(?P<pk>[0-9]+)/$', school_detail, name='school_detail'),
])

