from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Importando os modelos, schemas e a função de dependência
from models.client_models import Client
from schemas.client_schemas import ClientCreate, ClientUpdate, Client as ClientSchema
from database.dependencies import get_db

# Cria o router para as rotas de clientes
router = APIRouter(
    prefix="/clients",
    tags=["clients"],
    responses={404: {"description": "Not Found"}},
)

# Rota POST para criar um novo cliente
@router.post("/", response_model=ClientSchema, status_code=status.HTTP_201_CREATED)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = db.query(Client).filter(Client.email == client.email).first()
    if db_client:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    new_client = Client(**client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

# Rota GET para listar todos os clientes
@router.get("/", response_model=List[ClientSchema])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    clients = db.query(Client).offset(skip).limit(limit).all()
    return clients

# Rota GET para obter um cliente específico pelo ID
@router.get("/{client_id}", response_model=ClientSchema)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return client

# Rota PUT para atualizar um cliente específico
@router.put("/{client_id}", response_model=ClientSchema)
def update_client(client_id: int, client_update: ClientUpdate, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    update_data = client_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(client, key, value)

    db.commit()
    db.refresh(client)
    return client

# Rota DELETE para deletar um cliente específico
@router.delete("/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db.delete(client)
    db.commit()
    return
