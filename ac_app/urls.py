"""ac_tool URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings 
from ac_app import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^ac_app/',include('ac_app.urls')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'special/',views.special, name='special'),
    url(r'^handson_view/', views.handson_table, name="handson_view"),
    url(r'^embedded_handson_view_single/',views.embed_handson_table_from_a_single_table,name="embed_handson_view"),
    url(r'^download/', views.download, name='download')
]   

