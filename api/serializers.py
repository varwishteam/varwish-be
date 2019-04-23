from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.serializers import UserSerializer


class CustomRegisterSerializer(RegisterSerializer):
	username = serializers.CharField(required=True)
	first_name = serializers.CharField(max_length=50)
	last_name = serializers.CharField(max_length=50)

	def get_cleaned_data(self):
		return {
			'username': self.validated_data.get('username', ''),
			'first_name': self.validated_data.get('first_name', ''),
			'last_name': self.validated_data.get('last_name', ''),
			'password1': self.validated_data.get('password1', ''),
			'email': self.validated_data.get('email', ''),
		}

	def save(self, request):
		adapter = get_adapter()
		user = adapter.new_user(request)
		self.cleaned_data = self.get_cleaned_data()
		adapter.save_user(request, user, self)
		setup_user_email(request, user, [])
		user.save()
		return user


class TokenSerializer(serializers.ModelSerializer):
	user_type = serializers.SerializerMethodField()

	class Meta:
		model = Token
		fields = ('key', 'user', 'user_type')

	def get_user_type(self, obj):
		serializer_data = UserSerializer(
			obj.user
		).data
		return {
			'id': serializer_data.get('id'),
		}
