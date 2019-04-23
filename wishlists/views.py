from rest_framework import viewsets, renderers
from rest_framework.decorators import action, detail_route
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

	@detail_route(methods=['get', 'post', 'delete', 'put'], url_path='items', url_name='items')
	def items(self, request, pk):
		# wishlist = self.get_object()
		print(pk)
		# print(type(wishlist))
		queryset = Wishlist.objects.filter(id=pk)
		serializer = ItemDetailSerializer(queryset[0].items, many=True)
		# return Response(json.dumps(serializer.data, cls=UUIDEncoder))
		return Response(serializer.data)

	def create(self, request, *args, **kwargs):
		serializer = WishlistSerializer(data=request.data)
		if serializer.is_valid():
			wishlist = serializer.create(request)
			if wishlist:
				return Response(status=HTTP_201_CREATED)
		return Response(status=HTTP_400_BAD_REQUEST)


class ItemViewSet(viewsets.ModelViewSet):
	serializer_class = ItemDetailSerializer(Item)
	# queryset = Item.objects.all()

	# def get(self, request, uuid):
	# 	queryset = Item.objects.filter(id=uuid)
