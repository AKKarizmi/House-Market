from django.db import models

# Create your models here.

class House(models.Model):
	"""docstring for ClassName"""
	location = models.CharField(max_length=100)
	price = models.IntegerField()
	image = models.FileField()
	phone = models.IntegerField()
	rooms = models.IntegerField()
	floors = models.IntegerField()
	owner = models.CharField(max_length=20)

class Data(models.Model):
	"""docstring for """
	location = models.CharField(max_length=100)
	price = models.IntegerField()
	image = models.FileField()
	phone = models.IntegerField()
	rooms = models.IntegerField()
	floors = models.IntegerField()
	owner = models.CharField(max_length=20)

class Photo(models.Model):
	"""docstring for """
	mental = models.FileField()
	money = models.IntegerField()			


		