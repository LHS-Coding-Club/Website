import time

from fastapi import FastAPI, BackgroundTasks 
#from app.routes.auth import auth_router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="./app/frontend"), name="frontend")

def write_log():
    request_time = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(time.time()))
    log_file = open("logs.txt", "a")
    log_file.write(f"Request made at: {request_time}\n")
    log_file.close()

@app.get("/")
async def home(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log)
    return FileResponse("./app/frontend/html/home.html")

#app.include_router(auth_router, prefix="/auth")
