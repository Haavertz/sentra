#!/usr/bin/env python3 
class Database:
      def __init__(self):
          self.monitors: list[dict] = []

database = Database()

def get_session() -> Database:
    return database
