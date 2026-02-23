from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	course = models.CharField(max_length=60)

	def __str__(self):
		return self.name