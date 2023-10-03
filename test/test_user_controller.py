import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app

def test_app_creation(client):
    assert client is not None

def test_login_route(client):
    response = client.post('/api/auth/login')
    assert response.status_code == 200