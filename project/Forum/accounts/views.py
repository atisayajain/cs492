from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserBasicForm


def profile(request):

    # Login required
    if request.user.is_authenticated:
        return render(request, 'accounts/profile.html', {'user': request.user})
    else:
        return render(request, 'accounts/login.html')


def user_login(request):

    # Login required
	if not request.user.is_authenticated:
		if request.method == "POST":
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

            #If user is not banned
			if user is not None:
				if user.is_active:
					login(request, user)
					return render(request, 'accounts/profile.html')
				else:
					return render(request, 'accounts/register.html', {'error_message': 'The user is no longer active'})
		return render(request, 'accounts/login.html')
	return render(request, 'accounts/profile.html')

def user_register(request):

    #UserCreationForm(modified into UserBasicForm) does the password checking and other additionals for us
    form = UserBasicForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']   #password1 and password2(confirm_password) are the two variables in UserCreationForm 
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		return render(request, 'accounts/profile.html')
        	else:
        		return render(request, 'accounts/register.html', {'error_message': 'The user is no longer active.'})
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'accounts/login.html')


