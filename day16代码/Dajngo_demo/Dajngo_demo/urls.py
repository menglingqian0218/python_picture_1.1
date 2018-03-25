"""

Dajngo_demo URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^app01/', include('app01.urls')),
    url(r'^login_in/', views.login_in),

    url(r"^back",views.back)

    # url(r'^index/', views.index),
    # url(r'^login_in/', views.login_in),

    # 当路径符合多个url的时候，走第一个
    #url(r'^articles/\d{4}$', views.year2),   #   year_2004(request)
    #url(r'^articles/2004$', views.year_2004),   #   year_2004(request)

    # 无名参数
    #url(r'^articles/(\d{4})', views.year),     #    year(request,2010)
    #url(r'^articles/(\d{4})/(\d{2})', views.year_month),     #    year(request,2010,12)

    # 有名参数
    # url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.year_month),     #    year(request,year=2010,month=12)


]
