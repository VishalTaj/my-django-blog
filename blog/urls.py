from django.conf.urls import url
from . import views 

urlpatterns = [
               url(r'^$', views.post_list, name='post_list'),
               url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
               ]


# ^(?P<question_id>[0-9]+)/vote/