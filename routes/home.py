#!/usr/bin/env python3 
from fastapi import APIRouter, Request

router = APIRouter(
        tags=["home"]
)

@router.get("/")
def home_home(request: Request):
    context = {
        "request": request
    }
    #return template 
