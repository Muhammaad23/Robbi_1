from rest_framework import serializers
from .models import *


class MehmonxonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mehmonxona
        fields = ['id', 'title', 'image', 'job_time', 'address']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'  # Serialize all fields of the model
