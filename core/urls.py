"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# Rutas por módulo
import core_auth.router as auth_router
import core_user.router as user_router
import core_common.router as common_router

urlpatterns = [
    # Admin de Django
    path('admin/', admin.site.urls),

    # Autenticación JWT y rutas protegidas
    path('api/auth/', include(auth_router.urlpatterns)),

    # Endpoints de usuario
    path('api/user/', include(user_router.urlpatterns)),

    # Utilidades comunes (permisos, vistas protegidas, etc.)
    path('api/common/', include(common_router.urlpatterns)),

    # Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
