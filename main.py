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
    body = await request.body()
    if body:
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            return {"status": "error", "message": "El cuerpo debe ser JSON válido"}
    else:
        payload = {}
    subprocess.call(["/opt/bitnami/projects/backendFastAPI/deploy.sh"])
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
    return {"message": "API eCommerce 2026"}

