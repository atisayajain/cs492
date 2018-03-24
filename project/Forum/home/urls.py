from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [

	# home/
	url(r'^$', views.index, name='index'),

	# home/post/details/74/
	url(r'^post/details/(?P<post_id>[0-9]+)/', views.details, name='details'),

	# home/post/create_post/
	url(r'^post/create_post/', views.create_post, name='post-add'),

	# home/post/edit_post/
	url(r'^post/(?P<post_id>[0-9]+)/edit_post/', views.edit_post, name='post-edit'),

	# home/post/
	url(r'^post/(?P<post_id>[0-9]+)/delete_post/', views.delete_post, name='post-delete'),


]