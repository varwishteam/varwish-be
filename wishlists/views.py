from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import WishlistForm


# Create your views here.
def wishlists(request):
    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            new_wishlist = form.save()
            return HttpResponseRedirect('/wishlists/')
    else:
        form = WishlistForm()
    return render(request, 'wishlist.html', {'form':form})
