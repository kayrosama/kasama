from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core_user.models import Usuario
from core_user.serializers import UsuarioSerializer
from core_common.permissions import IsAdminOrSelf

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSelf]

