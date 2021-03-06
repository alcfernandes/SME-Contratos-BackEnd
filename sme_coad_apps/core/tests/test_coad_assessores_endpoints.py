import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_url_unauthorizade(client):
    response = client.get('/coad-assessores/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_url_authorized(authencticated_client):
    response = authencticated_client.get('/coad-assessores/')
    assert response.status_code == status.HTTP_200_OK
