from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserBasicForm(UserCreationForm):
	email = forms.EmailField(label = "Email")

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']


class UserInfoForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ['website', 'bio', 'profile_picture']
