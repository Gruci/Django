from django.conf.urls import url
from . import views #현재 폴터에서 views를 갖고와라

urlpatterns = [
    url(r'^$', views.index),
]