from rest_framework import serializers
from .models import Config, LichessConfigModel

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

class LichessConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LichessConfigModel
        fields = '__all__'