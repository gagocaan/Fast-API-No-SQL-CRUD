from fastapi import FastAPI

from .routes.student import router as StudentRouter

app = FastAPI(
    title="Backend de Prueba Mongo DB",
    description="CRUD con Mongo DB",
    version="0.1.0",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redocs",
    openapi_url="/api/v1/openapi.json",
    debug=False,
)


app.include_router(StudentRouter, tags=["Student"], prefix="/student")


@app.get("/healtz", tags=["Healtz"])
async def healtz():
    return {"message": "OK"}
