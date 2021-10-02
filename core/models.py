from django.db import models
from django.contrib.auth.models import User

LEVELS = (("0", "0"), ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))

# Create your models here.
class Buyer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Seller(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	level = models.CharField(choices=LEVELS, max_length=1, default=0)

class Microservice(models.Model):
	seller = models.ForeignKey('Seller', on_delete=models.CASCADE)
	# max 3 days
	delay = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 3 * 24)])
	price = models.PositiveIntegerField()
	description = models.TextField(max_length=32768)
	packages = models.ManyToManyField('Category')

class Package(models.Model):
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=255)
	price = models.PositiveIntegerField()

class Category(models.Model):
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=255)

class Type(models.Model):
	name = models.CharField(max_length=32)
	description = models.CharField(max_length=255)