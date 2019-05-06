from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_201_CREATED,
	HTTP_400_BAD_REQUEST
)

from .serializers import CategorySerializer, AttributeSerializer
from .models import Category, Attribute


class CategoryViewSet(viewsets.ModelViewSet):
	serializer_class = CategorySerializer
	queryset = Category.objects.all()


class AttributeViewSet(viewsets.ModelViewSet):
	serializer_class = AttributeSerializer

	def get_queryset(self):
		return Attribute.objects.filter(category=self.kwargs['_pk'])

	def create(self, request, *args, **kwargs):
		serializer = AttributeSerializer(data=request.data)
		if serializer.is_valid():
			attribute = serializer.create(request)
			if attribute:
				attribute = Attribute.objects.filter(id=attribute.id)
				attribute = AttributeSerializer(attribute.all(), many=True).data
				return Response(attribute, status=HTTP_201_CREATED)
		return Response(status=HTTP_400_BAD_REQUEST)
