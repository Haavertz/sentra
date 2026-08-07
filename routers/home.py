#!/usr/bin/env python3 
from fastapi import APIRouter, Request
from utils.html import templates
from db.client import get_session

router = APIRouter(
        tags=["home"]
)

@router.get("/")
def home_home(request: Request):
    session = get_session()
    context = {
        "request": request,
        "comments": session.comments
    }
    return templates.TemplateResponse(request, 'home/index.html', context) 
