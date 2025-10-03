from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core_user.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('x', include(router.urls)),
]
