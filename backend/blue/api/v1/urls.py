from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TruckViewSet

router = DefaultRouter()
router.register("truck", TruckViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
