from django.conf.urls import url

from . import views

app_name = 'Dreamerlixu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]