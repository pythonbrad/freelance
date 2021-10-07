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
			forms.instance.username = forms.instance.email
			forms.save()
			return redirect('login')
	else:
		forms = SigninForm()
	return render(request, 'core/signin.html', {'forms': forms, 'title': 'Signin'})

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
	return render(request, 'core/login.html', {'forms': forms, 'title': 'Login'})

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home', {'title': "Home"})


def details(request, pk):
	return render(request, 'core/details.html')

def about(request):
	return render(request, 'core/about_us.html', {'title': 'About'})

def become_seller(request):
	if request.user.is_authenticated:
		return render(request, 'core/become_seller.html', {'title': 'Become a seller'})
	else:
		return redirect('signin')

def buyer_account(request):
	if request.user.is_authenticated:
		return render(request, 'core/buyer_account.html', {'title': 'My buyer account'})
	else:
		return redirect('signin')

def seller_account(request):
	if request.user.is_authenticated:
		return render(request, 'core/seller_account.html', {'title': 'My seller account'})
	else:
		return redirect('signin')