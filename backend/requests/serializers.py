from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from .models import UserRequest

class UserRequestSerializer(FriendlyErrorMessagesMixin,
                            serializers.ModelSerializer):

    class Meta:
        model = UserRequest
        fields = '__all__'

