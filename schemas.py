from pydantic import BaseModel, Field, validator

class ProductoSchema(BaseModel):
    id: int | None = Field(None, description="ID del producto")
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre del producto")
    categoria: str = Field(..., min_length=3, max_length=50, description="Categoría del producto")
    valor: float = Field(..., gt=0, description="El valor debe ser mayor que cero")

    class Config:
        orm_mode = True
