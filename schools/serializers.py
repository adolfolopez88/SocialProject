from .models import School
from rest_framework import serializers 
from django.shortcuts import get_object_or_404
from courses.serializers import CourseSerializer

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
	courses = serializers.HyperlinkedRelatedField(many=True, view_name='courses_api:course_detail', read_only=True)
	
	class Meta:
		model = School
		fields = ('name', 'phone', 'address', 'image', 'url', 'courses', )
		extra_kwargs = {'url': {'view_name': 'schools_api:school_detail'}}

        