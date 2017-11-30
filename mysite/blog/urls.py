from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailedView.as_view(), name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_update'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_drafts'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment,name='add_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove,name='comment_delete'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish,name='post_publish'),
]
