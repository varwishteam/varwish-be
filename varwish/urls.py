from django.contrib import admin
from django.urls import path, include
from rest_auth.views import LoginView

from api.views import CustomRegisterView

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api-auth/', include('rest_framework.urls')),
	path('rest-auth/', include('rest_auth.urls')),
	path('rest-auth/registration/', include('rest_auth.registration.urls')),
	path('accounts/', include('allauth.urls')),

	path('login/', LoginView.as_view(), name='login'),
	path('register/', CustomRegisterView.as_view(), name='registration'),
]
