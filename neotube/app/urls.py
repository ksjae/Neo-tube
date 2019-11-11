from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^signup/$', views.signup , name='signup'),
    url(r'^search/$', views.SearchFormView, name='search'),
    url(r'^$',views.showvideo,name='showvideo'),
]