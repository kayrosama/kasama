from rest_framework.routers import DefaultRouter
from core_user.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = router.urls
