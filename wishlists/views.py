from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_201_CREATED,
	HTTP_400_BAD_REQUEST
)

from .serializers import WishlistSerializer, ItemDetailSerializer
from .models import Wishlist, Item


class WishlistsViewSet(viewsets.ModelViewSet):
	serializer_class = WishlistSerializer

	def get_queryset(self):
		user = self.request.user
		return Wishlist.objects.filter(user=user)

	def create(self, request, *args, **kwargs):
		serializer = WishlistSerializer(data=request.data)
		if serializer.is_valid():
			try:
				wishlist = serializer.create(request)
			except TypeError as te:
				return Response(te.args, status=HTTP_400_BAD_REQUEST)

			if wishlist:
				wishlist = Wishlist.objects.filter(id=wishlist.id)
				wishlist = WishlistSerializer(wishlist.all(), many=True).data
				return Response(wishlist, status=HTTP_201_CREATED)
		return Response(status=HTTP_400_BAD_REQUEST)


class ItemsViewSet(viewsets.ModelViewSet):
	serializer_class = ItemDetailSerializer

	def get_queryset(self):
		return Item.objects.filter(wishlist=self.kwargs['_pk'])

	def create(self, request, *args, **kwargs):
		serializer = ItemDetailSerializer(data=request.data)
		if serializer.is_valid():
			try:
				item = serializer.create(request)
			except TypeError as te:
				return Response(te.args, status=HTTP_400_BAD_REQUEST)

			if item:
				item = Item.objects.filter(id=item.id)
				item = ItemDetailSerializer(item.all(), many=True).data
				return Response(item, status=HTTP_201_CREATED)
		return Response(status=HTTP_400_BAD_REQUEST)
