from rest_framework import serializers


from .models import CustomUser
from wishlists.serializers import WishlistSerializer


class UserSerializer(serializers.ModelSerializer):
	wishlists = serializers.SerializerMethodField()

	class Meta:
		model = CustomUser
		fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'wishlists')

	def get_wishlists(self, obj):
		wishlists = WishlistSerializer(obj.user.all(), many=True).data
		return wishlists
