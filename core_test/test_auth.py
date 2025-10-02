import pytest
import time
from dotenv import dotenv_values
from rest_framework.test import APIClient
from core_user.models import CustomUser

# Cargar credenciales desde .env_test
credentials = dotenv_values(".env_test")
TEST_EMAIL = credentials.get("TEST_EMAIL")
TEST_PASSWORD = credentials.get("TEST_PASSWORD")
TEST_EMAIL_FAKE = credentials.get("TEST_EMAIL_FAKE")
TEST_PASSWORD_FAKE = credentials.get("TEST_PASSWORD_FAKE")

@pytest.mark.django_db
def test_jwt_login_success():
    CustomUser.objects.create_user(email=TEST_EMAIL, password=TEST_PASSWORD)
    client = APIClient()
    response = client.post("/api/auth/login/", {"email": TEST_EMAIL, "password": TEST_PASSWORD})
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_jwt_login_failure():
    client = APIClient()
    response = client.post("/api/auth/login/", {"email": TEST_EMAIL_FAKE, "password": TEST_PASSWORD_FAKE})
    assert response.status_code == 401

@pytest.mark.django_db
def test_jwt_token_refresh():
    CustomUser.objects.create_user(email=TEST_EMAIL, password=TEST_PASSWORD)
    client = APIClient()
    login_response = client.post("/api/auth/login/", {"email": TEST_EMAIL, "password": TEST_PASSWORD})
    refresh_token = login_response.data.get("refresh")
    assert refresh_token is not None

    refresh_response = client.post("/api/auth/refresh/", {"refresh": refresh_token})
    assert refresh_response.status_code == 200
    assert "access" in refresh_response.data
    
@pytest.mark.django_db
def test_token_expired():
    CustomUser.objects.create_user(email=TEST_EMAIL, password=TEST_PASSWORD)
    client = APIClient()
    response = client.post("/api/auth/login/", {"email": TEST_EMAIL, "password": TEST_PASSWORD})
    access_token = response.data.get("access")
    assert access_token is not None

    # Simular expiración (ajusta el tiempo según tu configuración de ACCESS_TOKEN_LIFETIME)
    time.sleep(2)

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    protected_response = client.get("/api/protected/")
    assert protected_response.status_code in [401, 403]

@pytest.mark.django_db
def test_access_protected_route():
    CustomUser.objects.create_user(email=TEST_EMAIL, password=TEST_PASSWORD)
    client = APIClient()
    response = client.post("/api/auth/login/", {"email": TEST_EMAIL, "password": TEST_PASSWORD})
    access_token = response.data.get("access")
    assert access_token is not None

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    protected_response = client.get("/api/protected/")
    assert protected_response.status_code == 200

@pytest.mark.django_db
def test_logout_token_blacklist():
    CustomUser.objects.create_user(email=TEST_EMAIL, password=TEST_PASSWORD)
    client = APIClient()
    response = client.post("/api/auth/login/", {"email": TEST_EMAIL, "password": TEST_PASSWORD})
    refresh_token = response.data.get("refresh")
    access_token = response.data.get("access")
    assert refresh_token is not None and access_token is not None

    # Simular logout (requiere configuración de blacklist en settings)
    logout_response = client.post("/api/auth/logout/", {"refresh": refresh_token})
    assert logout_response.status_code in [200, 205]

    # Intentar acceder con el token después del logout
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    protected_response = client.get("/api/protected/")
    assert protected_response.status_code in [401, 403]
    