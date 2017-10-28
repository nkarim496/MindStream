"""MindStream URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from minder import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^wimm/', include('wimm.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^(?P<username>[\w_]+)/$', views.minds, name='minds'),
    url(r'^(?P<username>[\w_]+)/minds/(?P<mind_id>[0-9]+)/delete/$', views.mind_del, name='mind_delete'),
    url(r'^(?P<username>[\w_]+)/minds/(?P<mind_id>[0-9]+)/edit/$', views.mind_edit, name='mind_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
