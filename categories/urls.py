from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import CategoryViewSet

router = DefaultRouter()
router.register(r'', CategoryViewSet, base_name='categories')

urlpatterns = router.urls
