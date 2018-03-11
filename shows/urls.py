from django.conf.urls import url, include
from . import views

urlpatterns = [
    # /shows/
    url(r'^$', views.index, name='index'),

    # /shows/1/
    url(r'^(?P<show_id>[0-9]+)/$', views.detail, name='detail'),
]
