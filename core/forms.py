from django import forms
from .models import User, Microservice


class SigninForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['last_name', 'first_name', 'email', 'password']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'name': 'last_name', 'placeholder': 'Last name'})
		self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'type': 'text', 'name': 'first_name', 'placeholder': 'First name'})
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'type': 'email', 'name': 'email', 'placeholder': 'Email'})
		self.fields['password'].widget.attrs.update({'class': 'form-control', 'type': 'password', 'name': 'password', 'placeholder': 'Password'})
	
	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email):
			self.add_error('email', 'This email is already used')
		else:
			pass
		return email

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'class': 'form-control', 'type': 'email', 'name': 'email', 'placeholder': 'Email'})
		self.fields['password'].widget.attrs.update({'class': 'form-control', 'type': 'password', 'name': 'password', 'placeholder': 'Password'})
	
	def clean(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		self.user = User.objects.filter(email=email)
		if self.user.exists():
			self.user = self.user.filter(password=password)
			if self.user.exists():
				pass
			else:
				self.add_error('password', 'Password invalid')
		else:
			self.add_error('email', 'Email invalid')

	def get_user(self):
		return self.user[0]

class MicroserviceForm(forms.ModelForm):
	class Meta:
		model = Microservice
		fields = ['name', 'description', 'price', 'delay', '_type']

	media = forms.ImageField()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'form-control'})
		self.fields['description'].widget.attrs.update({'class': 'form-control'})
		self.fields['price'].widget.attrs.update({'class': 'form-control'})
		self.fields['delay'].widget.attrs.update({'class': 'form-control'})
		self.fields['_type'].widget.attrs.update({'class': 'form-control'})
		self.fields['media'].widget.attrs.update({'class': 'form-control'})