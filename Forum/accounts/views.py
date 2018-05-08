from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserBasicForm, UserInfoForm
from .models import UserProfile


def profile(request, user_id):

    # Login required
    if request.user.is_authenticated:
        if user_id:
            user = User.objects.get(pk=user_id)
            return render(request, 'accounts/profile.html', {'user': user, 'user_now': request.user})
        else:    
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
    forminfo = UserInfoForm(request.POST or None)


    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']   #password1 and password2(confirm_password) are the two variables in UserCreationForm 
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()
        
        # Send Email notification
        subject = "Thank you for joining the College Forum, " + user.username
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        singup_message = """Welcome to RCCIIT College Forum."""
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=singup_message, fail_silently=False)

        user = authenticate(username=username, password=password)
        if user is not None:
        	if user.is_active:
        		login(request, user)
        		return render(request, 'accounts/add_info.html', {'form': forminfo})
        	else:
        		return render(request, 'accounts/register.html', {'error_message': 'The user is no longer active.'})
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'accounts/login.html')


def add_info(request):
    form = UserInfoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        info = form.save(commit=False)
        info.user = request.user
        role = form.cleaned_data['role']
        if role == "STUDENT":
            roll = form.cleaned_data['roll']
            if roll[0:4] == 'AEIE':
                    year = roll[4:8]
            elif roll[0:2] == 'IT':
                year = roll[2:6]
            else:
                year = roll[3:7]
        else:
            year = ""
        info.year = year
        info.save()
        return render(request, 'accounts/profile.html', {'user': request.user})

    return render(request, 'accounts/add_info.html', {'form': form})


def edit_info(request):

    if request.method == "POST":
        form = UserInfoForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)

        if form.is_valid():
            info = form.save(commit=False)
            info.user = request.user
            info.dept = form.cleaned_data['dept']
            info.role = form.cleaned_data['role']
            info.roll = form.cleaned_data['roll']
            info.save()
            return render(request, 'accounts/profile.html', {'user': request.user})
    else:
        form = UserInfoForm(instance=request.user.userprofile)
        return render(request, 'accounts/add_info.html', {'form': form})
