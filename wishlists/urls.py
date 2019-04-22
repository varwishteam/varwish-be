from django.urls import path
from wishlists import views

urlpatterns = [
    path('', views.WishlistList.as_view(), name='wishlist_list'),
    path('create', views.WishlistCreate.as_view(), name='wishlist_create'),
    path('update/<uuid:pk>', views.WishlistUpdate.as_view(), name='wishlist_update'),
    path('delete/<uuid:pk>', views.WishlistDelete.as_view(), name='wishlist_delete'),
    path('<uuid:pk>', views.WishlistDetail.as_view(), name='wishlist_detail'),
]
