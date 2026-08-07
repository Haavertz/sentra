#!/usr/bin/env python3 
from fastapi import APIRouter, Request
from utils.html import templates

router = APIRouter(
        tags=["home"]
)

@router.get("/")
def home_home(request: Request):
    context = {
        "request": request,
        "mydata": [1, 2, 3]
    }
    return templates.TemplateResponse(request, 'home/index.html', context) 
