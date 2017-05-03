from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url('', include('social_django.urls', namespace='social')),
	url(r'^', include('userprofiles.urls', namespace='userprofiles')),
	url(r'^', include('schools.urls', namespace='schools')),
	url(r'^', include('courses.urls', namespace='courses')),
    #url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),

    url(r'^users/logout/$', 
    	auth_views.logout, 
    	{'next_page': '/'}, 
    	name="user-logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
