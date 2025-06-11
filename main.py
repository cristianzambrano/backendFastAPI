from fastapi import FastAPI, Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from database import engine, Base, SessionLocal
from models import Producto
from schemas import ProductoSchema


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = SQLAlchemyCRUDRouter(
    schema=ProductoSchema,
    db_model=Producto,
    db=get_db,
    prefix="productos"
)

app.include_router(router)