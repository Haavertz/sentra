#!/usr/bin/env python3 
from fastapi import APIRouter, Depends, status, HTTPException
from utils.request_model import MonitorCreateData
from db.client import Database, get_session

router = APIRouter(
        prefix="/monitors",
        tags=["monitors"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_monitor( data: MonitorCreateData, session: Database = Depends(get_session) ):
  monitor_id = session.next_monitor_id
  session.next_monitor_id += 1

  monitor = {
      "id": monitor_id,
      **data.model_dump(mode="json"),
  }

  session.monitors[monitor_id] = monitor
  return monitor

@router.get("/")
def get_monitors(session: Database = Depends(get_session) ):
    return list(session.monitors.values())

@router.get("/{monitor_id}")
def get_monitor( monitor_id: int, session: Database = Depends(get_session) ):
  monitor = session.monitors.get(monitor_id)

  if monitor is None:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Monitor not found")

  return monitor

@router.delete("/{monitor_id}")
def delete_monitors(monitor_id: int, session: Database = Depends(get_session)):
    monitor = session.monitors.pop(monitor_id, None)
    if monitor is None:
        raise HTTPException(status_code=404, detail="Item not Found ")

    return { "message": "Monitor deleted", "monitor": monitor }
