from django.shortcuts import render
from rest_framework import  viewsets
from . import serializers, models
from . import mixins
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


class PartnershipAgriculturalView(mixins.ReadWriteSerializerMixin, viewsets.ModelViewSet):
    read_serializer_class = serializers.PartnershipAgriculturalSerializer
    write_serializer_class = serializers.PartnershipAgriculturalWriteSerializer

    model = models.PartnershipAgricultural
    
    def get_queryset(self):

        if 'farmer' in self.request.GET:
            farmer = self.request.GET['farmer']
            return models.PartnershipAgricultural.objects.filter(farmer=farmer)

        elif 'agricultural' in self.request.GET:
            agricultural = self.request.GET['agricultural']
            return models.PartnershipAgricultural.objects.filter(agricultural=agricultural)

        return models.PartnershipAgricultural.objects.all()


class PartnershipFarmView(mixins.ReadWriteSerializerMixin, viewsets.ModelViewSet):
    read_serializer_class = serializers.PartnershipFarmSerializer
    write_serializer_class = serializers.PartnershipFarmWriteSerializer
    model = models.PartnershipFarm

    def get_queryset(self):

        if 'farm' in self.request.GET:
            farm = self.request.GET['farm']
            return models.PartnershipFarm.objects.filter(farm=farm)

        elif 'farmer' in self.request.GET:
            farmer = self.request.GET['farmer']
            return models.PartnershipFarm.objects.filter(farmer=farmer)

        elif 'agricultural' in self.request.GET:
            agricultural = self.request.GET['agricultural']
            return models.PartnershipFarm.objects.filter(agricultural=agricultural)

        return models.PartnershipFarm.objects.all()


class CadespViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CadespSerialier
    model = models.Cadesp

    def get_queryset(self):

        if 'farm' in self.request.GET:
            farm = self.request.GET['farm']
            return models.Cadesp.objects.filter(farm=farm)

        elif 'farmer' in self.request.GET:
            farmer = self.request.GET['farmer']
            return models.Cadesp.filter(farmer=farmer)

        return models.Cadesp.objects.all()