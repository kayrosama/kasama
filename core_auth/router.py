from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CustomTokenObtainPairView,
    LogoutView,
    ProtectedAdminView,
    protected_view,
    ProtectedClassView,
    protected_decorator_view,
)

urlpatterns = [
    # Autenticación JWT
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='token_logout'),

    # Rutas protegidas (originales)
    path('protected-class/', ProtectedAdminView.as_view(), name='protected_class'),
    path('protected-decorator/', protected_view, name='protected_decorator'),

    # Rutas protegidas (nuevas con permisos y decoradores separados)
    path('protected-role-class/', ProtectedClassView.as_view(), name='protected_role_class'),
    path('protected-role-decorator/', protected_decorator_view, name='protected_role_decorator'),
]
