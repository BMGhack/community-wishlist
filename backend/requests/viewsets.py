from rest_framework import viewsets
from .serializers import UserRequestSerializer
from .models import UserRequest

class UserRequestViewSet(viewsets.ModelViewSet):
    queryset = UserRequest.objects.all()
    serializer_class = UserRequestSerializer
