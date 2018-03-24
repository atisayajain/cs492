from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
	
	# accounts/
	url(r'^$', views.user_login, name='login'),

	# accounts/register
	url(r'^register$', views.user_register, name='register'),

	# accounts/register_additional
	url(r'register/additional$', views.user_additional, name='register-additional'),

	# accounts/profile
	url(r'^profile$', views.profile, name='profile'),

	# accounts/logout
	url(r'^logout$', views.user_logout, name='logout'),


]