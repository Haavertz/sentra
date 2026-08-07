#!/usr/bin/env python3
""" Html related assets """

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import main 

def mount_static():
    main.app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
