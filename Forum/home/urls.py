from django.conf.urls import url, include
from . import views

app_name = 'home'

urlpatterns = [

	# home/
	url(r'^$', views.index, name='index'),

	# home/post/details/74/
	url(r'^post/details/(?P<post_id>[0-9]+)/', views.details, name='details'),

	# home/post/create_post/
	url(r'^post/create_post/', views.create_post, name='post-add'),

	# home/post/74/edit_post/
	url(r'^post/(?P<post_id>[0-9]+)/edit_post/', views.edit_post, name='post-edit'),

	# home/post/74/delete_post/
	url(r'^post/(?P<post_id>[0-9]+)/delete_post/', views.delete_post, name='post-delete'),

	# home/post/74/add_comment/
	url(r'^post/(?P<post_id>[0-9]+)/add_comment/', views.add_comment, name='add-comment'),

	# home/post/74/delete_comment/23/
	url(r'^post/(?P<post_id>[0-9]+)/delete_comment/(?P<comment_id>[0-9]+)/$', views.delete_comment, name='delete-comment'),

	# home/search/
	url(r'^search$', views.search, name='search'),

]