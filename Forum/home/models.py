from django.contrib.auth.models import User
from django.db import models

DEPARTMENT_CHOICES = (
		('ALL', 'ALL'),
		('CSE', 'CSE'),
		('ECE', 'ECE'),
		('IT', 'IT'),
		('EE', 'EE'),
		('AEIE', 'AEIE'),
	)

YEAR_CHOICES = (
		('ALL', 'ALL'),
		('2014', '2014'),
		('2015', '2015'),
		('2016', '2016'),
		('2017', '2017'),
	)

class Post(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	photo = models.FileField(blank=True, upload_to='posts')
	content = models.TextField()
	dept = models.CharField(max_length=5, choices=DEPARTMENT_CHOICES, default='ALL')
	year = models.CharField(max_length=4, choices=YEAR_CHOICES, default='ALL')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	time_now = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	body = models.TextField()
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.user.username