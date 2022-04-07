from .models import VehicleType, Vehicle, Journey, ServiceArea
from rest_framework import serializers

class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class JourneySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journey
        fields = '__all__'

class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'