from django.conf.urls import url
from . import views #현재 폴터에서 views를 갖고와라

urlpatterns = [
    url(r'^$', views.index),
    url(r'^areas/(?P<area>[가-힣]+)/$',views.areas),
    url(r'^areas/(?P<area>[가-힣]+)/results$',views.results),
    url(r'^polls/(?P<poll_id>\d+)/$',views.polls)
]