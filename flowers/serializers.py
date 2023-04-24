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