"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
admin.autodiscover()
import blog.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/index/(?P<id>\d{2})$', blog.views.index),
    url(r'^blog/index1/(?P<id>\d{2})$', blog.views.index1),
    url(r'^blog/index2/(?P<id>\d{2})$', blog.views.index2),
    url(r'^blog/db/(?P<type>\d{1})$', blog.views.db_ctrl),
#     
    url(r'^upload/(?P<type>\d{1})$', blog.views.upload),
#     
    url(r'^reg$', blog.views.reg),
    url(r'^login$', blog.views.login),
    url(r'^showUser$', blog.views.showUser),
    url(r'^logout$', blog.views.logout),
]
