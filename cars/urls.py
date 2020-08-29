from django.urls import path, include
from rest_framework import routers
from cars.views import CarViewSet, RateCarView, PopularCarView

router = routers.DefaultRouter()
router.register('cars', CarViewSet, basename='cars')
router.register('rate', RateCarView, basename='rate')
router.register('popular', PopularCarView, basename='popular')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]