from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^signup/$', views.signup , name='signup'),
    url(r'^search/$', views.SearchFormView, name='search'),
    url(r'^video/$',views.showvideo,name='showvideo'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]