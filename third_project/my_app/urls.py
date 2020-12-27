from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from my_app import views

# Template Tagging
app_name = 'my_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^testpage/$', views.test, name='test_page'),
    url(r'^register/$', views.register, name='registration'),
    url(r'^user_login/$', views.user_login, name='user_login')
]
