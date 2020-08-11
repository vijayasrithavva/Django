from django.db import models

# Create your models here.
class Emp(models.Model):
	"""docstring for Emp"""
	empId = models.CharField(max_length=10)
	empName= models.CharField(max_length=30)
	empDesig = models.CharField(max_length=30)
	salary= models.FloatField()

	def __str__(self):
		return self.empId+' '+self.empName
	
	