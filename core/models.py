from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

LEVELS = (("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))

# Create your models here.
class Headshot(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	media = models.ImageField(upload_to='user_headhosts')

	def __str__(self):
		return f'Headshot of {user}'

class Buyer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user)

class Seller(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	level = models.CharField(choices=LEVELS, max_length=1, default="0")
	active = models.BooleanField(default=False)

	def __str__(self):
		return str(self.user)

class Microservice(models.Model):
	seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	# max 3 days
	delay = models.PositiveIntegerField(choices=[(i, f"{i} hours") for i in range(1, 3 * 24 + 1)])
	price = models.PositiveIntegerField(choices=[(i, f"{i} kolos") for i in range(2, 100 + 1)], default=2)
	description = models.TextField(max_length=32768)
	packages = models.ManyToManyField('Package')
	_type = models.ForeignKey('Type', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Command(models.Model):
	buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE)
	microservice = models.ForeignKey('Microservice', on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)
	mark = models.PositiveIntegerField(default=1, choices=((i,i) for i in range(1, 6)))
	valided = models.BooleanField(default=False)

class Illustration(models.Model):
	microservice = models.ForeignKey("Microservice", on_delete=models.CASCADE)
	media = models.ImageField(upload_to='microservice_illustrations')

	def __str__(self):
		return self.microservice

class Package(models.Model):
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=255)
	price = models.PositiveIntegerField()

	def __str__(self):
		return self.name

class Type(models.Model):
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=255)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=255)

	def __str__(self):
		return self.name