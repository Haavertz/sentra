#!/usr/bin/env python3 
from typing import List

class Database:
    comments: List[str] = []

database = Database()

def get_session() -> Database:
    return database
