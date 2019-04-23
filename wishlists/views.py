from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_201_CREATED,
	HTTP_400_BAD_REQUEST
)
import json
from uuid import UUID

from .serializers import WishlistSerializer, ItemDetailSerializer
from .models import Wishlist, Item


class UUIDEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, UUID):
			return obj.hex
		return json.JSONEncoder.default(self, obj)


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


class ItemsViewSet(viewsets.ModelViewSet):
	serializer_class = ItemDetailSerializer

	def get_queryset(self):
		for i in self.kwargs:
			print(i)
		return Item.objects.filter(wishlist=self.kwargs['_pk'])
