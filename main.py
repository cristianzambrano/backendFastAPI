from fastapi import FastAPI, Request
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from database import engine, Base, SessionLocal
from models import Producto
from schemas import ProductoSchema

import json

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Despliegue de Aplicaciones Web y CI/CD en AWS")

import subprocess
import logging
from fastapi import Request, HTTPException

logger = logging.getLogger(__name__)

import subprocess
from fastapi import Request, HTTPException

@app.post("/webhook")
async def webhook(request: Request):
    # Validar aquí la firma de GitHub y la rama main.

    result = subprocess.run(
        ["sudo", "-n", "systemctl", "start", "--no-block",
         "fastapi-deploy.service"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise HTTPException(
            status_code=500,
            detail="No se pudo iniciar el despliegue"
        )

    return {"status": "deploy solicitado"}

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
    return {"message": "API eCommerce 2026 con FastAPI y SQLAlchemy. Despliegue de Aplicaciones Web y CI/CD en AWS."}

