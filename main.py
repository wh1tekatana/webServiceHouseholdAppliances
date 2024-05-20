from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.routers import router
from app.database import engine, Base

# Создание всех таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def main():
    return FileResponse("templates/index.html")
