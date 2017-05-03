from django.db import models

# Create your models here.
class School(models.Model):
	name = models.CharField(max_length=255)
	phone = models.IntegerField()
	address = models.CharField(max_length=255)
	image = models.ImageField(blank=True)

	def __str__(self):
		return self.name
