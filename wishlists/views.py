from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_201_CREATED,
	HTTP_400_BAD_REQUEST
)

from .serializers import WishlistSerializer
from .models import Wishlist


class WishlistsViewSet(viewsets.ModelViewSet):
	serializer_class = WishlistSerializer
	queryset = Wishlist.objects.all()

	def create(self, request, *args, **kwargs):
		serializer = WishlistSerializer(data=request.data)
		if serializer.is_valid():
			wishlist = serializer.create(request)
			if wishlist:
				return Response(status=HTTP_201_CREATED)
		return Response(status=HTTP_400_BAD_REQUEST)
