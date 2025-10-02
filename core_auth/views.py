from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core_auth.models import Rol
from core_auth.serializers import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]
