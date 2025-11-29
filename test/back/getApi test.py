import requests
import pytest

BASE_URL = "https://reqres.in/api"

@pytest.mark.api
def test_get_user_exitoso():
    """
    Consulta un usuario existente y valida que responda 200 y datos correctos.
    """
    response = requests.get(f"{BASE_URL}/users/2")

    assert response.status_code == 200

    data = response.json()
    assert data["data"]["id"] == 2
    assert data["data"]["first_name"] == "Janet"
    assert data["data"]["email"].endswith("@reqres.in")


@pytest.mark.api
def test_get_user_inexistente_devuelve_404():
    """
    Consulta un usuario que no existe y valida que responda 404.
    """
    response = requests.get(f"{BASE_URL}/users/99999")

    assert response.status_code == 404