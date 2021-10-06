from django.shortcuts import render, reverse, redirect
from .models import Microservice
from .forms import SigninForm, LoginForm
from django.contrib import auth

# Create your views here.
def index(request, tag=None):
	return render(request, 'core/index.html', {'title': 'Home', 'microservices': Microservice.objects.all()})

def signin(request):
	if request.user.is_authenticated:
		return redirect('home')
	elif request.POST:
		forms = SigninForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('login')
	else:
		forms = SigninForm()
	return render(request, 'core/signin.html', {'forms': forms})

def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	elif request.POST:
		forms = LoginForm(request.POST)
		if forms.is_valid():
			user = forms.get_user()
			auth.login(request, user)
			return redirect('home')
	else:
		forms = LoginForm()
	return render(request, 'core/login.html', {'forms': forms})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')


def details(request, pk):
	return render(request, 'core/details.html')

def about(request):
	return render(request, 'core/about_us.html')

def become_seller(self):
	if request.user.is_authenticated:
		pass
	else:
		return redirect('signin')