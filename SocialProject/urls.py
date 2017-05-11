from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework.authtoken import views
from . import views as main_views

urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
	url('', include('social_django.urls', namespace='social')),
	url(r'^', include('userprofiles.urls', namespace='userprofiles')),

    #schools
	url(r'^', include('schools.urls', namespace='schools')),
    url(r'^api/v1/', include('schools.api_urls', namespace='schools_api')),

    #courses
	url(r'^', include('courses.urls', namespace='courses')),
    url(r'^api/v1/', include('courses.api_urls', namespace='courses_api')),

    #rest_framework
    url(r'^api/v1/$', main_views.api_root),
 	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^users/logout/$', 
    	auth_views.logout, 
    	{'next_page': '/'}, 
    	name="user-logout"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^api/v1/auth', include('rest_framework.urls', namespace='api_rest'))
]