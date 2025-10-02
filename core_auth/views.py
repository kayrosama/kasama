from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from .serializers import CustomTokenObtainPairSerializer
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

    def get(self, request):
        return Response({"message": "Acceso autorizado por clase de permiso"})


@api_view(['GET'])
@require_role(['admin', 'owner'])
def protected_decorator_view(request):
    """
    Vista protegida usando decorador personalizado.
    """
    return Response({"message": "Acceso autorizado por decorador"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    Logout con blacklist de refresh token.
    """
    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"detail": "Sesión cerrada"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception:
        return Response({"detail": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)
        