from fastapi import FastAPI
from routers import home, monitors
from utils.html import mount_static

app = FastAPI()

mount_static()

app.include_router(home.router)
app.include_router(monitors.router)
