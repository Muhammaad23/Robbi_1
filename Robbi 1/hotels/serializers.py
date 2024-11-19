from rest_framework import serializers
from .models import Hotels

class HotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotels
        fields = '__all__'  # Serialize all fields of the model
