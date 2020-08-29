from django.urls import path, include
from rest_framework import routers
from cars.views import CarViewSet

router = routers.DefaultRouter()
router.register('cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]