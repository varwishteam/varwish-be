from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import include, re_path

from .views import WishlistsViewSet, ItemsViewSet

router = DefaultRouter()
router.register(r'', WishlistsViewSet, base_name='wishlists')

wishlists_router = routers.NestedDefaultRouter(router, r'', lookup='')
wishlists_router.register(r'items', ItemsViewSet, base_name='wishlist-items')

urlpatterns = [
	re_path(r'^', include(router.urls)),
	re_path(r'^', include(wishlists_router.urls)),
]
