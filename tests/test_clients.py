import pytest
from fastapi import status

def test_create_client(client):
    client_data = {
        "name": "João Silva",
        "email": "joao.silva@example.com",
        "phone": "11999999999"
    }
    response = client.post("/clients/", json=client_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["id"] is not None
    assert data["name"] == client_data["name"]
    assert data["email"] == client_data["email"]
    assert data["phone"] == client_data["phone"]

def test_create_client_existing_email(client):
    client_data = {
        "name": "Maria Souza",
        "email": "maria.souza@example.com",
        "phone": "11888888888"
    }
    response = client.post("/clients/", json=client_data)
    assert response.status_code == status.HTTP_201_CREATED

    response = client.post("/clients/", json=client_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "Email já cadastrado"

def test_read_clients(client):
    clients = [
        {"name": "Cliente 1", "email": "cliente1@example.com", "phone": "11111111111"},
        {"name": "Cliente 2", "email": "cliente2@example.com", "phone": "22222222222"},
        {"name": "Cliente 3", "email": "cliente3@example.com", "phone": "33333333333"},
    ]
    for c in clients:
        client.post("/clients/", json=c)

    response = client.get("/clients/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 3
    for i, c in enumerate(clients):
        assert data[i]["name"] == c["name"]
        assert data[i]["email"] == c["email"]
        assert data[i]["phone"] == c["phone"]

def test_read_client(client):
    client_data = {
        "name": "Carlos Pereira",
        "email": "carlos.pereira@example.com",
        "phone": "11444444444"
    }
    response = client.post("/clients/", json=client_data)
    assert response.status_code == status.HTTP_201_CREATED
    client_id = response.json()["id"]

    response = client.get(f"/clients/{client_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == client_id
    assert data["name"] == client_data["name"]
    assert data["email"] == client_data["email"]
    assert data["phone"] == client_data["phone"]

def test_read_client_not_found(client):
    response = client.get("/clients/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Cliente não encontrado"

def test_update_client(client):
    client_data = {
        "name": "Ana Paula",
        "email": "ana.paula@example.com",
        "phone": "11555555555"
    }
    response = client.post("/clients/", json=client_data)
    assert response.status_code == status.HTTP_201_CREATED
    client_id = response.json()["id"]

    update_data = {
        "name": "Ana P.",
        "phone": "11666666666"
    }
    response = client.put(f"/clients/{client_id}", json=update_data)
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == client_id
    assert data["name"] == update_data["name"]
    assert data["email"] == client_data["email"]
    assert data["phone"] == update_data["phone"]

def test_delete_client(client):
    client_data = {
        "name": "Pedro Gomes",
        "email": "pedro.gomes@example.com",
        "phone": "11777777777"
    }
    response = client.post("/clients/", json=client_data)
    assert response.status_code == status.HTTP_201_CREATED
    client_id = response.json()["id"]

    response = client.delete(f"/clients/{client_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response = client.get(f"/clients/{client_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
