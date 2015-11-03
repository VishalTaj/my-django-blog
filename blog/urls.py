from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView


urlpatterns = [
               url(r'^$', PostListView.as_view()),
               url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post_detail'),
               url(r'^new/$', views.post_new , name='post_new'),
               url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
               ]



# ^(?P<question_id>[0-9]+)/vote/
