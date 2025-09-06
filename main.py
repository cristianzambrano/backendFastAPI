from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter

from database import engine, Base, SessionLocal
from models import Producto
from schemas import ProductoSchema

# Crear tablas en MySQL si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Productos con MySQL")

# Dependencia de sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD automático 🚀
router = SQLAlchemyCRUDRouter(
    schema=ProductoSchema,   # Modelo Pydantic
    db_model=Producto,       # Modelo SQLAlchemy
    db=get_db,               # Sesión
    prefix="productos"
)

app.include_router(router)
