from .models import Course
from rest_framework import serializers 
from schools import serializers as SchoolsSerializers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	school = serializers.ReadOnlyField(source='owner.name')

	class Meta:
		model = Course
		fields = ('name', 'school', 'url', )
		extra_kwargs = {'url': {'view_name': 'courses_api:course_detail'}}
