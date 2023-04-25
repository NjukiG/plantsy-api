from django.contrib.auth import get_user_model  # new
from rest_framework import serializers

from .models import Flowers

class FlowersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "image",
            "description",
            "price",
            "is_in_stock",
            "created_at",
        )
        model = Flowers


class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)