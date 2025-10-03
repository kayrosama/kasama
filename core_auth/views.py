from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .serializers import CustomTokenObtainPairSerializer, LogoutSerializer
from .permissions import IsAdminOrOwner
from .decorators import require_role


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Login con JWT usando email.
    """
    serializer_class = CustomTokenObtainPairSerializer


class ProtectedClassView(APIView):
    """
    Vista protegida usando clase de permiso personalizada.
    """
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    @extend_schema(
        responses={200: {"type": "object", "properties": {"message": {"type": "string"}}}},
        description="Vista protegida con clase de permiso personalizada"
    )
    def get(self, request):
        return Response({"message": "Acceso autorizado por clase de permiso"})


class ProtectedDecoratorView(APIView):
    """
    Vista protegida usando decorador personalizado.
    """
    permission_classes = [IsAuthenticated]

    @require_role(['admin', 'owner'])
    @extend_schema(
        responses={200: {"type": "object", "properties": {"message": {"type": "string"}}}},
        description="Vista protegida usando decorador personalizado"
    )
    def get(self, request):
        return Response({"message": "Acceso autorizado por decorador"})


class LogoutView(APIView):
    """
    Logout con blacklist de refresh token.
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=LogoutSerializer,
        responses={
            205: {"type": "object", "properties": {"detail": {"type": "string"}}},
            400: {"type": "object", "properties": {"detail": {"type": "string"}}}
        },
        description="Logout con blacklist de refresh token"
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if serializer.is_valid():
            try:
                refresh_token = serializer.validated_data["refresh"]
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"detail": "Sesión cerrada"}, status=status.HTTP_205_RESET_CONTENT)
            except Exception:
                return Response({"detail": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        