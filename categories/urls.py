from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from django.urls import include, re_path

from .views import CategoryViewSet, AttributeViewSet


router = DefaultRouter()
router.register(r'', CategoryViewSet, base_name='categories')
category_router = routers.NestedDefaultRouter(router, r'', lookup='')
category_router.register(r'attributes', AttributeViewSet, base_name='category-attributes')

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^', include(category_router.urls)),
]
