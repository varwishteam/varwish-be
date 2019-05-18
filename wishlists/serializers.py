from rest_framework import serializers

from .models import Wishlist, Item
from categories.models import Category
from users.models import CustomUser


class StringSerializer(serializers.StringRelatedField):
	def to_internal_value(self, val):
		return val


class ItemDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Item
		fields = ('id', 'item_name', 'category', 'wishlist', 'note', 'amount', 'price', 'link', 'status')

	def create(self, request):
		data = request.data
		category = data.pop('category')
		wishlist = data.pop('wishlist')
		item = Item.objects.create(**data)
		item.category = Category.objects.filter(id=category).get()
		item.wishlist = Wishlist.objects.filter(id=wishlist).get()
		item.save()

		wishlist = Wishlist.objects.filter(id=wishlist).get()
		wishlist.status = 'op'
		wishlist.save()

		return item


class WishlistSerializer(serializers.ModelSerializer):

	class Meta:
		model = Wishlist
		fields = ('id', 'name', 'description', 'user', 'status', 'items')

	user = StringSerializer(many=False)
	items = serializers.SerializerMethodField()

	def get_items(self, obj):
		items = ItemDetailSerializer(obj.items.all(), many=True).data
		return items

	def create(self, request):
		data = request.data
		user = data.pop('user')
		items = data.pop('items')
		wishlist = Wishlist.objects.create(**data)
		wishlist.user = CustomUser.objects.filter(id=user).get()

		for item in items:
			category = item.pop('category')
			item = wishlist.items.create(**item)
			item.category = Category.objects.filter(id=category).get()
			item.save()

		wishlist.save()
		return wishlist
