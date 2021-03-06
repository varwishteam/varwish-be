from django.db import models


class Attribute(models.Model):
	category = models.ForeignKey(
		'Category',
		on_delete=models.CASCADE,
		null=False,
		blank=False,
		related_name='attributes',
	)

	name = models.CharField(max_length=50, null=False, blank=False)
	type = models.CharField(max_length=50, null=True, blank=True, default=None)  # basic setup, will be updated to another field type
	value = models.CharField(max_length=50, blank=True, default=None)  # field type based on Attribute.type

	def __str__(self):
		return self.name


class Category(models.Model):

	class Meta:
		verbose_name_plural = "categories"

	name = models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return self.name
