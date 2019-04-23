from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from wishlists.models import Wishlist


class CustomUserManager(UserManager):
	pass


class CustomUser(AbstractUser):
	objects = CustomUserManager()
	wishlists = models.ManyToManyField(Wishlist, related_name='wishlists')

	def __str__(self):
		return self.username
