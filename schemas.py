from pydantic import BaseModel, Field, validator

class ProductoSchema(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre del producto")
    descripcion: str = Field(..., min_length=15,max_length=20, description="Descripción detallada")
    precio: float = Field(..., gt=0, description="Precio debe ser mayor que cero")

    class Config:
        orm_mode = True
