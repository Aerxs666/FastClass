# AI Knowledge Assistant - Bootstrap API

Primer incremento funcional (Módulo 0): API asíncrona con FastAPI,
validada con Pydantic y probada con pytest. **No integra ningún LLM.**

## Requisitos
- Python 3.12+
- Git

## Instalación
```bash
git clone https://github.com/Aerxs666/FastClass.git
cd FastClass
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Linux / macOS
source .venv/bin/activate

pip install -e ".[dev]"
```

## Ejecutar la API
```bash
fastapi dev
# o: uvicorn app.main:app --reload
```
Swagger: http://127.0.0.1:8000/docs

## Endpoints
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /health | Estado del servicio |
| POST | /api/v1/chat | Respuesta bootstrap (`answer`, `provider`) |
| GET | /api/v1/info | Información del proyecto |

## Pruebas
```bash
python -m pytest -q
```

## Demos asíncronas
```bash
python scripts/asyncio_demo.py
# con la API corriendo en otra terminal:
python scripts/httpx_demo.py
```
