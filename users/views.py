from rest_framework import viewsets

from .models import CustomUser
from .serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = CustomUser.objects.all()
