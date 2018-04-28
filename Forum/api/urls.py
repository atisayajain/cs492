from django.conf.urls import url
from .views import PostRudView, CommentRudView, PostListView, ProfileRudView

app_name = 'api-postings'

urlpatterns = [

	# /api/postings/post/
	url(r'^post/$', PostListView.as_view(), name='post-list'),

	#/api/postings/post/74/
	url(r'^post/(?P<pk>[0-9]+)/$', PostRudView.as_view(), name='post-rud'),

	# /api/postings/comment/74/
	url(r'^comment/(?P<pk>[0-9]+)/$', CommentRudView.as_view(), name='comment-rud'),

	#/api/postings/profile/72/
	url(r'^profile/(?P<pk>[0-9]+)/$', ProfileRudView.as_view(), name='profile-rud'),

]