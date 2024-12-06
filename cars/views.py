from rest_framework import viewsets, permissions
from .models import Cars
from .serializers import CarSerializers

class CarViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializers
    permission_classes = [permissions.AllowAny]
