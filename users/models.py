from django.db import models

# Create your models here.

class Pancake(models.Model):
	kj = models.FileField()
	sd = models.IntegerField()

class me(models.Model):
	live = models.TextField()
	main = models.TextField()
	about = models.CharField(max_length=1000)
	name = models.CharField(max_length=100)
