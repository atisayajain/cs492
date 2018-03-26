from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
	
	# accounts/
	url(r'^$', views.user_login, name='login'),

	# accounts/register
	url(r'^register$', views.user_register, name='register'),

	# accounts/addinfo
	url(r'^add_info$', views.add_info, name='add-info'),

	# accounts/editinfo
	url(r'^edit_info$', views.edit_info, name='edit-info'),

	# accounts/profile/3/
	url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),

	# accounts/logout
	url(r'^logout$', views.user_logout, name='logout'),


]