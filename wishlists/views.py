from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_201_CREATED,
	HTTP_400_BAD_REQUEST
)

from .forms import WishlistForm
from .serializers import WishlistSerializer
from .models import Wishlist


def wishlists(request):
	if request.method == 'POST':
		form = WishlistForm(request.POST)
		if form.is_valid():
			new_wishlist = form.save()
			return HttpResponseRedirect('/wishlists/')
	else:
		form = WishlistForm()
	return render(request, 'wishlist.html', {'form': form})


class WishlistsViewSet(viewsets.ModelViewSet):
	serializer_class = WishlistSerializer
	queryset = Wishlist.objects.all()

	def create(self, request):
		serializer = WishlistSerializer(data=request.data)
		if serializer.is_valid():
			wishlist = serializer.create(request)
			if wishlist:
				return Response(status=HTTP_201_CREATED)
		return Response(status=HTTP_400_BAD_REQUEST)
