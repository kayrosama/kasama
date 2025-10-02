import os

# Create necessary directories
os.makedirs('core_user', exist_ok=True)
os.makedirs('core_auth', exist_ok=True)

# Content for core_user/views.py
core_user_views = '''from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core_user.models import Usuario
from core_user.serializers import UsuarioSerializer
from core_common.permissions import IsAdminOrSelf

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSelf]
'''

# Content for core_user/serializers.py
core_user_serializers = '''from rest_framework import serializers
from core_user.models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'rol']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
'''

# Content for core_user/router.py
core_user_router = '''from rest_framework.routers import DefaultRouter
from core_user.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = router.urls
'''

# Content for core_auth/views.py
core_auth_views = '''from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from core_auth.models import Rol
from core_auth.serializers import RolSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated]
'''

# Content for core_auth/serializers.py
core_auth_serializers = '''from rest_framework import serializers
from core_auth.models import Rol

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'descripcion']
'''

# Content for core_auth/router.py
core_auth_router = '''from rest_framework.routers import DefaultRouter
from core_auth.views import RolViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet, basename='rol')

urlpatterns = router.urls
'''

# Write files to core_user
with open('core_user/views.py', 'w') as f:
    f.write(core_user_views)

with open('core_user/serializers.py', 'w') as f:
    f.write(core_user_serializers)

with open('core_user/router.py', 'w') as f:
    f.write(core_user_router)

# Write files to core_auth
with open('core_auth/views.py', 'w') as f:
    f.write(core_auth_views)

with open('core_auth/serializers.py', 'w') as f:
    f.write(core_auth_serializers)

with open('core_auth/router.py', 'w') as f:
    f.write(core_auth_router)

print("Archivos base generados exitosamente en core_user y core_auth.")
