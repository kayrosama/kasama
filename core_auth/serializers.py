from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer personalizado para login con JWT usando email.
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({"user_id": self.user.id, "email": self.user.email})
        return data

class LogoutSerializer(serializers.Serializer):
    """
    Serializer para recibir el refresh token en el logout.
    """
    refresh = serializers.CharField()
    