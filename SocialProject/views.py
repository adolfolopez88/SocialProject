from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
    	'schools': reverse('schools_api:school_list', request=request, format=format),
    	'courses': reverse('courses_api:course_list', request=request, format=format),
    })