from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class CustomUserManager(UserManager):
	pass


class CustomUser(AbstractUser):
	objects = CustomUserManager()
