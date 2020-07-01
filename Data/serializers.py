from rest_framework import serializers
from .models import Bank


class IfscSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields="__all__"
