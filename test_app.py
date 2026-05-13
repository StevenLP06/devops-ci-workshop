import app

def test_home():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "devops-api"

def test_health():
    client = app.app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    # Tu app retorna cpu_percent y memory_percent, no uptime_seconds
    assert "cpu_percent" in data
    assert "memory_percent" in data
    assert data["status"] in ["healthy", "unhealthy"]

def test_metric():
    client = app.app.test_client()
    response = client.get('/metric')  # Cambiado de /metrics a /metric
    assert response.status_code == 200
    # El texto retornado debe contener app_cpu_percent
    assert "app_cpu_percent" in response.data.decode()
