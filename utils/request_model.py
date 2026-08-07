#!/usr/bin/env python3 
""" Restructure these helper type methods in your own way if you want """

from pydantic import BaseModel

class CommentCreateData(BaseModel):
    content: str
