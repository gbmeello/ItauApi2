from fastapi import FastAPI
from routers import clients_routers


app = FastAPI()


app.include_router(clients_routers.router)
