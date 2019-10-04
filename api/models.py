from django.db import models


class Farmer(models.Model):
    name = models.CharField(max_length=128)
    cpf = models.CharField(max_length=13)


class Farm(models.Model):
    name = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=16)
    nirf = models.CharField(max_length=25)
    ccir = models.CharField(max_length=25)


class Cadesp(models.Model):
    farmer = models.ForeignKey('api.Farmer', on_delete=models.CASCADE)
    farm = models.ForeignKey('api.Farm', on_delete=models.CASCADE)
    nirf = models.CharField(max_length=25)
    ccir = models.CharField(max_length=25)
    hectar_nirf = models.DecimalField()
    hectar_ccir = models.DecimalField()


class Agricultural(models.Model):
    name = models.CharField(max_length=128)
    cnpj = models.CharField(max_length=16)


