import pytest
from rest_framework.test import APIClient
from core_user.models import CustomUserManager

@pytest.mark.django_db
def test_jwt_login_success():
    user = CustomUserManager.objects.create_user(email="useruno@kmkz.io", password="PorLaGranPuta#69.")
    client = APIClient()
    response = client.post("/api/auth/login/", {"email": "master@kmkz.io", "password": "Kinteki."})
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_jwt_login_failure():
    client = APIClient()
    response = client.post("/api/auth/login/", {"email": "master@kmkz.com", "password": "Kinteki."})
