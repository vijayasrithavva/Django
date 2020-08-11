from django.db import models

# Create your models here.
class demo(models.Model):
	"""docstring for demo"""
	name = models.CharField(max_length=20)
	age = models.IntegerField()