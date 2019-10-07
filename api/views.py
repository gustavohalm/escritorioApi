from django.shortcuts import render
from rest_framework import  viewsets
from . import serializers, models
# Create your views here.


class FarmerView(viewsets.ModelViewSet):
    serializer_class = serializers.FarmerSerializer
    model = models.Farmer
    queryset = models.Farmer.objects.all()


class FarmView(viewsets.ModelViewSet):
    serializer_class = serializers.FarmSerializer
    model = models.Farm
    queryset = models.Farm.objects.all()


class AgriculturalView(viewsets.ModelViewSet):
    serializer_class = serializers.AgriculturalSerializer
    model = models.Agricultural
    queryset = models.Agricultural.objects.all()


class PartnershipAgriculturalView(viewsets.ModelViewSet):
    serializer_class = serializers.PartnershipAgriculturalSerializer
    model = models.PartnershipAgricultural

    def get_queryset(self):
        return models.PartnershipAgricultural.objects.all()


class PartnershipFarmView(viewsets.ModelViewSet):
    serializer_class = serializers.PartnershipFarmSerializer
    model = models.PartnershipFarm

    def get_queryset(self):
        return models.PartnershipFarm.objects.all()
