
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views


urlpatterns = [


    # url(r'^index/', views.index),

    #
    # # 当路径符合多个url的时候，走第一个
    # url(r'^articles/\d{4}$', views.year2),   #   year_2004(request)
    # url(r'^articles/2004$', views.year_2004),   #   year_2004(request)

    # 无名参数
    #url(r'^articles/(\d{4})', views.year),     #    year(request,2010)
    url(r'^articles/(\d{4})/(\d{2})', views.year_month),     #    year(request,2010,12)

    # 有名参数
    #url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})', views.year_month),     #    year(request,year=2010,month=12)




     # get发送数据

    url(r"sendByget",views.sendByget)
]
