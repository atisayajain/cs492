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
	roll = models.CharField(max_length=11, default='RollYearNNN')
	profile_picture = models.ImageField(upload_to='profile_picture', blank=True)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Student')
	dept = models.CharField(max_length=5, choices=DEPARTMENT_CHOICES, default='CSE')
	year = models.CharField(max_length=4, default='2018')
	

	def __str__(self):
		return self.user.username
