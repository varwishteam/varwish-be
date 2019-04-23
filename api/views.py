from rest_auth.registration.views import RegisterView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CustomRegisterSerializer
from users.models import CustomUser
from wishlists.models import Wishlist


class CustomRegisterView(RegisterView):
	serializer_class = CustomRegisterSerializer


class ResetUsersView(APIView):
	def get(self, request):
		reset = CustomUser.objects.exclude(username='superuser').delete()
		return Response(
			{
				'User left': reset
			}
		)


class ResetWLView(APIView):
	def get(self, request):
		reset = Wishlist.objects.all().delete()
		return Response('all deleted')
