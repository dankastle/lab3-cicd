from app.main import app

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_parcela_sin_config():
    client = app.test_client()
    response = client.get("/parcela")
    assert response.status_code == 200
    assert response.get_json()["nombre"] == "sin-nombre"
