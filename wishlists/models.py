import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from categories.models import Category


class Wishlist(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	name = models.CharField(max_length=50, null=False, blank=False)
	description = models.CharField(max_length=200, null=True, blank=True)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		null=False,
		blank=False,
		related_name='user',
	)

	EMPTY = 'em'
	OPEN = 'op'
	COMPLETED = 'co'
	CLOSED = 'cl'

	WISHLIST_STATUS = (
		(EMPTY, 'Empty'),
		(OPEN, 'Open'),
		(COMPLETED, 'Completed'),
		(CLOSED, 'Closed')
	)

	status = models.CharField(
		max_length=2,
		choices=WISHLIST_STATUS,
		default=EMPTY
	)

	def __str__(self):
		return self.name


class Item(models.Model):
	item_name = models.CharField(max_length=50)
	note = models.CharField(max_length=200)
	link = models.URLField()
	amount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
	price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
	wishlist = models.ForeignKey(
		Wishlist,
		on_delete=models.CASCADE,
		blank=False,
		null=False,
		related_name='items',
	)

	WANTED = 'want'
	PURCHASED = 'purc'

	ITEM_STATUS = (
		(WANTED, 'Wanted'),
		(PURCHASED, 'Purchased'),
	)

	status = models.CharField(
		max_length=4,
		choices=ITEM_STATUS,
		default=WANTED
	)

	category = models.ForeignKey(
		Category,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		default=None,
		related_name='category_items'
	)

	def __str__(self):
		return self.item_name
