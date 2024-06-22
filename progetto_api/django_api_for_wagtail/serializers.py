# django_api_for_wagtail/serializers.py
from rest_framework import serializers
from .models import Nation

class NationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = '__all__'
