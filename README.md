# Ejemplo de CRUD MongoDB con Fast API

## Ejecutar

```bash
docker-compose --env-file .env up --build
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
