from src.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "Smart Deployment Notifier" in data["message"]

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"

def test_version():
    client = app.test_client()
    response = client.get('/api/version')
    assert response.status_code == 200
    data = response.get_json()
    assert data["version"] == "1.0.0"
    assert data["app"] == "Smart Deployment Notifier"
