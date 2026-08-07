#!/usr/bin/env python3 
from fastapi import APIRouter, Depends, status
from utils.request_model import MonitorCreateData
from db.client import Database, get_session

router = APIRouter(
        prefix="/monitors",
        tags=["monitors"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_monitor(data: MonitorCreateData, session: Database = Depends(get_session) ):
    monitor = {
      "id": len(session.monitors) + 1,
      **data.model_dump(mode="json"),
    }

    session.monitors.append(monitor)
    return monitor

@router.get("/")
def get_monitors(session: Database = Depends(get_session) ):
    return session.monitors


