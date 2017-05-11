from django.db import models
from schools.models import School

class Course(models.Model):
	name = models.CharField(max_length=255)
	min_months = models.IntegerField() 
	school = models.ForeignKey(School, related_name='courses')

	class Meta:
		unique_together = ('school',)

	def __str__(self):
		return self.name

		 

