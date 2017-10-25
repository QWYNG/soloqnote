from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.form_test, name='views.form_test'),
    url(r'^form$', views.form_test),
]
