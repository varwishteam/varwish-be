from django.urls import path
from .views import ResetUsersView, ResetWLView

urlpatterns = [
    path('reset/users/', ResetUsersView.as_view(), name='login'),
    path('reset/wl/', ResetWLView.as_view(), name='login'),
]
