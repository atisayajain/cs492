from django.contrib.auth.models import User
from django.db import models

ROLE_CHOICES = (
		('STUDENT', 'Student'),
		('TEACHER', 'Teacher'),
	)
DEPARTMENT_CHOICES = (
		('CSE', 'CSE'),
		('ECE', 'ECE'),
		('IT', 'IT'),
		('EE', 'EE'),
		('AEIE', 'AEIE'),
	)

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	website = models.URLField(blank=True)
	bio = models.TextField(blank=True)
	profile_picture = models.ImageField(upload_to='profile_picture', blank=True)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
	dept = models.CharField(max_length=5, choices=DEPARTMENT_CHOICES, default='CSE')
	
	def __str__(self):
		return self.user.username
