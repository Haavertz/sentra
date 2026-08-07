#!/usr/bin/env python3 
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from utils.request_model import CommentCreateData
from db.client import get_session

router = APIRouter(
        tags=["api", "comments"],
        prefix="/api/comment"
)

@router.post("/create")
def api_comment_create(data: CommentCreateData):
    session = get_session()
    session.comments.append(data.content)
    return JSONResponse({ "message" : session.comments })
