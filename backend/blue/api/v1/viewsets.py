from rest_framework import authentication
from blue.models import Truck
from .serializers import TruckSerializer
from rest_framework import viewsets


class TruckViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Truck.objects.all()
