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


class AgriculturalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agricultural
        fields = '__all__'
        read_only_fields = ['id', ]


class PartnershipAgriculturalSerializer(serializers.ModelSerializer):
    agricultural = AgriculturalSerializer(many=False)
    farmer = FarmerSerializer(many=False)

    class Meta:
        model = models.PartnershipAgricultural
        fields = '__all__'
        read_only_fields = ['id',]


class PartnershipFarmSerializer(serializers.ModelSerializer):
    farm = FarmSerializer(many=False)
    agricultural = AgriculturalSerializer(many = False, allow_null=True)
    farmer = FarmerSerializer(many= False, allow_null=True)

    class Meta:
        model = models.PartnershipFarm
        fields = '__all__'
        read_only_fields = ['id', ]