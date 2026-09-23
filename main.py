from fastapi import FastAPI, Request
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from database import engine, Base, SessionLocal
from models import Producto
from schemas import ProductoSchema

import json
import subprocess

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Despliegue de Aplicaciones Web y CI/CD en AWS")

@app.post("/webhook")
async def webhook(request: Request):
    subprocess.run( ["/bin/bash", "/opt/bitnami/projects/backendFastAPI/deploy.sh"], check=True )
    return {"status": "ok"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD automático para el modelo Producto
router = SQLAlchemyCRUDRouter(
    schema=ProductoSchema,   
    db_model=Producto,       
    db=get_db,               
    prefix="productos"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "API eCommerce 2026 - Despliegue de Aplicaciones Web y CI/CD en AWS"}

