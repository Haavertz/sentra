#!/usr/bin/env python3 
class Database:
      def __init__(self):
          self.monitors: dict[int, dict] = {}
          self.next_monitor_id = 1

database = Database()

def get_session() -> Database:
    return database
