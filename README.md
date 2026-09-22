# backendFastAPI

Este proyecto es una API CRUD de **productos** usando **FastAPI**, **SQLAlchemy** y **MySQL**.  
Se incluyen validaciones con Pydantic y un CRUD automático gracias a `fastapi-crudrouter`.  

---

## Requisitos

- Python 3.13 o anterior.
- MySQL en ejecución.

`fastapi-crudrouter==0.8.6` utiliza Pydantic 1.x. Python 3.14 no es compatible
con esta combinación de dependencias, por lo que debes usar Python 3.13 o una
versión anterior.

## Instalación y uso

### 1. Clona el repositorio
```bash
git clone https://github.com/cristianzambrano/backendFastAPI
cd backendFastAPI
```

### 2. Crea un entorno virtual
En **Windows (CMD)**:

```cmd
deactivate
rmdir /s /q venv
py -3.13 -m venv venv
venv\Scripts\activate
```

Si la carpeta `venv` todavía no existe, puedes ignorar el comando `rmdir`.

En **macOS o Linux**:

```bash
deactivate
rm -rf venv
python3.13 -m venv venv
source venv/bin/activate
```

### 3. Configura las variables de entorno
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (ajusta a tu configuración local de MySQL):

```ini
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=tienda
```

### 4. Instala las dependencias
```bash
pip install -r requirements.txt
```

No actualices Pydantic a la versión 2 mientras uses
`fastapi-crudrouter==0.8.6`, porque esa versión del router no es compatible
con Pydantic 2.

📌 Dependencias principales:
- **fastapi** → Framework de la API.
- **uvicorn** → Servidor ASGI para FastAPI.
- **sqlalchemy** → ORM para interactuar con MySQL.
- **pymysql** → Driver de MySQL para Python.
- **python-dotenv** → Para leer el archivo `.env`.
- **fastapi-crudrouter** → Generación automática de rutas CRUD.

### 5. Ejecuta el servidor local
```bash
uvicorn main:app --reload
```

La API quedará disponible en:
- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📌 Endpoints disponibles

Los endpoints generados automáticamente son:

| Método | Ruta             | Descripción                  |
|--------|------------------|------------------------------|
| GET    | `/productos`     | Listar todos los productos   |
| GET    | `/productos/{id}`| Obtener un producto por ID   |
| POST   | `/productos`     | Crear un nuevo producto      |
| PUT    | `/productos/{id}`| Actualizar un producto       |
| DELETE | `/productos/{id}`| Eliminar un producto         |

🔹 Además, se agregó un endpoint **PATCH** manual para actualizaciones parciales:

| Método | Ruta             | Descripción                        |
|--------|------------------|------------------------------------|
| PATCH  | `/productos/{id}`| Actualizar parcialmente un producto |

---

## 🛠 Notas
- La tabla `productos` en MySQL se define con `id INT AUTO_INCREMENT PRIMARY KEY`.
- Mantén el archivo `.gitignore` para excluir `venv/`, `.env` y archivos innecesarios.  
- Recomendado usar **Docker** o un servicio MySQL local para pruebas.  

---

## 👤 Autor

**Cristian Zambrano**  
📧 Email: cristian_uteq@hotmail.com

---