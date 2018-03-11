from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	website = models.URLField(blank=True)
	bio = models.TextField(blank=True)
	
	def __str__(self):
		return self.user.username
