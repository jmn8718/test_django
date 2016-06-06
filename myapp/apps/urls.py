from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<app_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^edit/(?P<app_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^list/public$', views.public, name='public'),
    url(r'^list/private$', views.private, name='private'),
]