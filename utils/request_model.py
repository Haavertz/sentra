#!/usr/bin/env python3 
""" Restructure these helper type methods in your own way if you want """

from pydantic import BaseModel, HttpUrl

class MonitorCreateData(BaseModel):
    name: str
    url: HttpUrl
