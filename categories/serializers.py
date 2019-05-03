from rest_framework import serializers

from .models import Category, Attribute
from wishlists.serializers import ItemDetailSerializer


class StringSerializer(serializers.StringRelatedField):
	def to_internal_value(self, val):
		return val


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ('id', 'name', 'items', 'attributes')

	items = serializers.SerializerMethodField()
	attributes = serializers.SerializerMethodField()

	def get_items(self, obj):
		items = ItemDetailSerializer(obj.category_items.all(), many=True).data
		return items

	def get_attributes(self, obj):
		attributes = AttributeSerializer(obj.attributes.all(), many=True).data
		return attributes


class AttributeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Attribute
		fields = '__all__'

	category = StringSerializer(many=False)

	def create(self, request):
		data = request.data
		category = data.pop('category')
		attribute = Attribute.objects.create(**data)
		attribute.category = Category.objects.filter(id=category).get()
		attribute.save()
		return attribute
