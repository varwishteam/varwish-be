from allauth.account.views import LoginView
from django.urls import path

urlpatterns = [
    path('api/', LoginView.as_view(), name='login'),
]