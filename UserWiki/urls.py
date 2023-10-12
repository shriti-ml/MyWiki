# from django.conf.urls import url
from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup$', views.signup, name="signup"),
    url(r"^signup/validate$", views.signup_validate, name="signup_validate"),
    url(r'^login$', views.c_login, name="login"),
    url(r"^login/validate$", views.login_validate, name="login_validate"),
    url(r'^logout$', views.c_logout, name="logout"),
    url("wikiinfo", views.wikiinfo, name= "Wiki Information")

]
