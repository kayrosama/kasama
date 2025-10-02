from rest_framework.permissions import BasePermission

class IsAdminOrSelf(BasePermission):
    """
    Permite acceso si el usuario es admin o si está accediendo a su propio recurso.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user.rol == 'admin' or obj == request.user
        )
        