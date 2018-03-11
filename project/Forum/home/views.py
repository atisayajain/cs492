from django.shortcuts import render


def index(request):

	# Login Required
	if request.user.is_authenticated:
		return render(request, 'home/index.html')
	else:
		return render(request, 'accounts/login.html')
