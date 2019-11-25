from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views, forms

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^signup/$', views.signup , name='signup'),
    url(r'^search/$', views.SearchFormView.as_view(), name='search'),
    url(r'^video/$',views.uploadvideo, name='upload'),
    url(r'^login/$', auth_views.LoginView.as_view(
            template_name="registration/login.html"
            ), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), 
    url(r'^view/$',views.VideoDetailView.as_view(), name='view'),
]