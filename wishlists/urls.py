from django.urls import path
from wishlists import views

urlpatterns = [
    path('', views.wishlists, name='wishlists'),
]