import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.mark.django_db
def test_add_value(api_client):
    url = "http://127.0.0.1:8000/values"
    response = api_client.post(url, {"value": "This value is for testing Add value"})
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_value(api_client):
    url = "http://127.0.0.1:8000/values"
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_principals(api_client):
    url = "http://127.0.0.1:8000/principals"
    data = {"principal": "This principal is for testing "}
    response = api_client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_principals(api_client):
    url = "http://127.0.0.1:8000/principals"
    response = api_client.get(url)
    assert response.status_code == 200

