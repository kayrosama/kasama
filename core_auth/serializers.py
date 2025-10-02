from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core_user.models import CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Campos personalizados en el token
        token['email'] = user.email
        token['rol'] = user.rol
        return token

    def validate(self, attrs):
        # Usamos email como identificador
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)
