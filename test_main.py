from fastapi.testclient import TestClient
from main import app # Importamos tu API

client = TestClient(app)

def test_read_main():
    # Simulamos una petición a la raíz
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API de Finanzas para Freelancers"}

def test_get_balance():
    # Probamos el endpoint que creamos para tu balance
    response = client.get("/balance")
    assert response.status_code == 200
    assert "balance" in response.json()