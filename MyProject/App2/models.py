from django.db import models

# Create your models here.
class Languages(models.Model):
	Language = models.CharField(max_length=20,null=True)
	inventor = models.CharField(max_length=20,null=True)
	date = models.DateField(null=True)
	location = models.CharField(max_length=30,null=True)

	def __str__(self):
	 	return self.Language+self.inventor+' '+str(self.date)+' '+self.location
class Mobiles(models.Model):
	model = models.CharField(max_length=30)
	cost = models.FloatField()
	year = models.IntegerField()

	def __str__(self):
		return self.model + ' '+ str(self.cost)

class Library(models.Model):
	bookName = models.CharField(max_length=30)
	department = models.CharField(max_length=30)
	author = models.CharField(max_length=30)
	year = models.IntegerField()

	def __str__(self):
		return self.bookName + ' ' + self.department + ' ' + self.author + ' ' + str(self.year)