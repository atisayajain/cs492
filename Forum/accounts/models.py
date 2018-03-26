from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	website = models.URLField(blank=True)
	bio = models.TextField(blank=True)
	profile_picture = models.ImageField(upload_to='profile_picture', blank=True)
	
	def __str__(self):
		return self.user.username
