"""gproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from Aapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 
    url(r'^log/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	 url(r'^register/$', views.register, name='register'),
	 url(r'^tinymce/', include('tinymce.urls')),
#	 url(r'^profile/$', views.server_profile, name='profile'),
  url(r'^$', views.server_list, name='server_list'),
  url(r'^new$', views.server_create, name='server_new'),
  url(r'^Article$', views.server_create1, name='server_new1'),
#  url(r'^update$', views.server_lprofile, name='server_lprofile1'),
  url(r'^Update Article$', views.server_create2, name='server_new2'),
  url(r'^edit/(?P<pk>\d+)$', views.server_update, name='server_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server_delete'),
  
]
if settings.DEBUG: 
			urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

