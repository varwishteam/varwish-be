from rest_framework import serializers

from .models import Category
from wishlists.serializers import ItemDetailSerializer


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Category
		fields = ('id', 'name', 'items')

	items = serializers.SerializerMethodField()

	def get_items(self, obj):
		items = ItemDetailSerializer(obj.category_items.all(), many=True).data
		return items
