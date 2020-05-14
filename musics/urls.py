from django.conf.urls import url
from . import views

app_name = "music"

urlpatterns = [
    # /musics/
    url(r'^$', views.index, name='index'),

    # /musics/1002
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
]