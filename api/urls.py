from django.urls import path, include
from rest_framework import routers
from . import  views
router = routers.DefaultRouter()

router.register('farmer', views.FarmerView, base_name='farmer_endpoint')
router.register('farm', views.FarmView, base_name='farm_endpoint')
router.register('agricultural', views.AgriculturalView, base_name='agricultural_endpoint')
router.register('parternership-farm', views.PartnershipFarmView, base_name='partnershipfarm_endpoint')
router.register('parternership-agricultural', views.PartnershipAgriculturalView, base_name='partnershipagri_endpoint')


urlpatterns = [
    path('', include(router.urls)),
]