from rest_framework import  serializers
from . import models


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Farmer
        fields = '__all__'
        read_only_fields = ['id',]


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Farm
        fields = '__all__'
        read_only_fields = ['id',]


class Agricultural(serializers.ModelSerializer):
    class Meta:
        model = models.Agricultural
        fields = '__all__'
        read_only_fields = ['id', ]
