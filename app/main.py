from fastapi import FastAPI

from app.routes.auth import auth_router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="./app/frontend"), name="frontend")

@app.get("/")
async def home():
    return FileResponse("./app/frontend/html/home.html")

app.include_router(auth_router, prefix="/auth")
