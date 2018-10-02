from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.summoner_name_form, name='views.summoner_name_form'),
    url(r'^form$', views.summoner_name_form),
]
