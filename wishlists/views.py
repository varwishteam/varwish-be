from django.core import serializers as to_json
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
	queryset = Wishlist.objects.all()

	def create(self, request, *args, **kwargs):
		serializer = WishlistSerializer(data=request.data)
		if serializer.is_valid():
			wishlist = serializer.create(request)
			if wishlist:
				wishlist = Wishlist.objects.filter(id=wishlist.id)
				wishlist = WishlistSerializer(wishlist.all(), many=True).data
				return Response(wishlist, status=HTTP_201_CREATED)
		return Response(status=HTTP_400_BAD_REQUEST)


class ItemsViewSet(viewsets.ModelViewSet):
	serializer_class = ItemDetailSerializer

	def get_queryset(self):
		for i in self.kwargs:
			print(i)
		return Item.objects.filter(wishlist=self.kwargs['_pk'])
>>>>>>> e180f5382824762c408eb53f4c3102c1d4483785
