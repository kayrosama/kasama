from rest_framework.routers import DefaultRouter
from core_auth.views import RolViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet, basename='rol')

urlpatterns = router.urls
