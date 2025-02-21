# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_get_price(client):
    rv = client.get('/price/BTCUSDT')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'status' in json_data
    assert 'price' in json_data

def test_analyze_market(client):
    rv = client.get('/analyze/BTCUSDT')
    json_data = rv.get_json()
    assert rv.status_code == 200
    assert 'status' in json_data
    if json_data['status'] == 'success':
        assert 'analysis' in json_data
        assert 'chart_data' in json_data