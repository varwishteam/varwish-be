from rest_framework.routers import DefaultRouter
from .views import WishlistsViewSet

router = DefaultRouter()
router.register(r'', WishlistsViewSet, base_name='wishlists')
urlpatterns = router.urls




