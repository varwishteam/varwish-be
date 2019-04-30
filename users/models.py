from django.contrib.auth.models import AbstractUser, UserManager

from wishlists.models import Wishlist


class CustomUserManager(UserManager):
	pass


class CustomUser(AbstractUser):
	objects = CustomUserManager()

	def __str__(self):
		return self.username
