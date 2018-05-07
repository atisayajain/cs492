from django.conf.urls import url
from .views import (
	PostRudView, 
	CommentRudView, 
	PostListView, 
	ProfileRudView, 
	CommentListView,
	ProfileListView
	)

app_name = 'api-postings'

urlpatterns = [

	# /api/postings/post/
	url(r'^post/$', PostListView.as_view(), name='post-list'),

	#/api/postings/post/74/
	url(r'^post/(?P<pk>[0-9]+)/$', PostRudView.as_view(), name='post-rud'),

	# /api/postings/comment/
	url(r'^comment/$', CommentListView.as_view(), name='comment-list'),

	# /api/postings/comment/74/
	url(r'^comment/(?P<pk>[0-9]+)/$', CommentRudView.as_view(), name='comment-rud'),

	# /api/postings/profile/
	url(r'^profile/$', ProfileListView.as_view(), name='profile-list'),

	#/api/postings/profile/72/
	url(r'^profile/(?P<user_id>[0-9]+)/$', ProfileRudView.as_view(), name='profile-rud'),

]