from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def require_role(allowed_roles):
    """
    Decorador para verificar si el usuario tiene uno de los roles permitidos.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return Response({"detail": "Autenticación requerida"}, status=status.HTTP_401_UNAUTHORIZED)
            if user.rol not in allowed_roles:
                return Response({"detail": "Acceso denegado"}, status=status.HTTP_403_FORBIDDEN)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
    