#!/usr/bin/env python3 
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

router = APIRouter(
        tags=["api", "comments"],
        prefix="/api/comment"
)

@router.post("/create")
def api_comment_create():
    return JSONResponse({ "message" : "ok" })
