from rest_framework import serializers
from .models import Backend


class BackendSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Backend