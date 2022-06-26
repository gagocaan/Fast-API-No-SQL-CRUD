# Ejemplo de CRUD MongoDB con Fast API

## Ejecutar

```bash
docker-compose --env-file .env up --build
```

## Consumir

### Validar que el servicio esta activo

```http
GET http://localhost:8000/healtz HTTP/1.1
content-type: application/json
```

### Documentacion

```http
GET http://localhost:8000/api/v1/docs HTTP/1.1
content-type: application/json
```

## Limpiar

```bash
docker-compose down
```

## Estructura

```bash
.
├── Dockerfile
├── README.md
├── app
│   ├── main.py
│   └── server
│       ├── app.py
│       ├── database.py
│       ├── models
│       │   └── student.py
│       └── routes
│           └── student.py
├── docker-compose.yaml
├── poetry.lock
└── pyproject.toml
```
