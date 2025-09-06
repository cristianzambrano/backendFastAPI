from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from database import engine, Base, SessionLocal
from models import Producto
from schemas import ProductoSchema

Base.metadata.create_all(bind=engine)

app = FastAPI(title="eCommerce BIU 2025 API Productos")

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
    return {"message": "Commerce BIU 2025 API Productos"}