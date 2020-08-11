from django.db import models

# Create your models here.
class Student(models.Model):
	branches = [('CSE','cse'),
				('ECE','ece'),
				('MECH', 'mech'),
				('IT', 'it')
	]
	studId = models.CharField(max_length=10)
	studName = models.CharField(max_length=30)
	branch = models.CharField(max_length=20,choices=branches)
	age = models.IntegerField()
		