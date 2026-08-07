from fastapi import FastAPI
from routers import home, api
from utils.html import mount_static
from db.client import database

app = FastAPI()

mount_static()

app.include_router(home.router)
app.include_router(api.router)
