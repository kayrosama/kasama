from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    LogoutView,
    ProtectedClassView,
    ProtectedDecoratorView,
)

urlpatterns = [
    # Autenticación JWT
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='token_logout'),

    # Rutas protegidas actualizadas
    path('protected-role-class/', ProtectedClassView.as_view(), name='protected_role_class'),
    path('protected-role-decorator/', ProtectedDecoratorView.as_view(), name='protected_role_decorator'),
]
