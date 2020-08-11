from django.db import models

# Create your models here.
class demo(models.Model):
	"""docstring for demo"""
	name = models.CharField(max_length=20)#,null=True)
	age = models.IntegerField(blank=True,default=20)#null=True)
	branch = models.CharField(max_length=10)
	def __str__(self):
		return self.name +' '+ str(self.age) 