from .models import Car
from rest_framework import serializers

class CarSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Car
        fields = '__all__'  # Corrected 'fiels' to 'fields'
