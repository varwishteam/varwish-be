from rest_framework import serializers

from .models import Wishlist, Item
from users.models import CustomUser


class StringSerializer(serializers.StringRelatedField):
	def to_internal_value(self, val):
		return val


class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('id', 'item_name', 'wishlist')


class WishlistSerializer(serializers.ModelSerializer):
	items = serializers.SerializerMethodField()
	user = StringSerializer(many=False)

	class Meta:
		model = Wishlist
		fields = ('id', 'name', 'description', 'user', 'status', 'items')

	def get_items(self, obj):
		items = ItemSerializer(obj.items.all(), many=True).data
		return items

	def create(self, request):
		"""
		{
			"id": "f95ea100-6547-11e9-a923-1681be663d3e",
			"name": "Postman-wishlist",
			"description": "lorem ipsum blablablablabla",
			"status": "op",
			"user": 4,
			"items": [
				{
					"item_name": "NOTEBOOK",
					"note": "MUDDD",
					"link": "https://notebook.com",
					"amount": 12,
					"price": 12000
				},
				{
					"item_name": "NOTEBOOK_2",
					"note": "WHUUUT",
					"link": "https://idontknow.com",
					"amount": 12,
					"price": 120000
				}
			]
		}
		"""
		data = request.data
		wishlist = Wishlist()
		wishlist.id = request.POST.get('id', None)
		user = CustomUser.objects.get(id=data['user'])
		wishlist.user = user
		wishlist.name = data['name']
		wishlist.description = data['description']
		wishlist.status = data['status']
		wishlist.save()

		# todo: assign the wishlist to user ( user.wishlists.add(wishlist) )

		for item in data['items']:
			new_item = Item()
			new_item.item_name = item['item_name']
			new_item.note = item['note']
			new_item.link = item['link']
			new_item.amount = item['amount']
			new_item.price = item['price']
			new_item.wishlist = wishlist
			new_item.save()
			wishlist.items.add(new_item)
		wishlist.save()
		return wishlist
