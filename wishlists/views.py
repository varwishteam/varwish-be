from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy

from .models import Wishlist


# Create your views here.
class WishlistList(generic.ListView):
    model = Wishlist


class WishlistCreate(CreateView):
    model = Wishlist
    fields = ['name', 'description']


class WishlistUpdate(UpdateView):
    model = Wishlist
    fields = ['name', 'description']


class WishlistDelete(DeleteView):
    model = Wishlist
    success_url = reverse_lazy('wishlist_list')


class WishlistDetail(generic.DetailView):
        model = Wishlist
