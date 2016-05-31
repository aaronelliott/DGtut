from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cshome', views.cs_home, name='cs_home'),
    url(r'^wipreq', views.cs_wipreq, name='cs_wipreq'),
    url(r'^wiplog', views.cs_wiplog, name='cs_wiplog'),
    ]
