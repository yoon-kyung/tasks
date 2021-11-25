from fastapi import Depends, Request, APIRouter
from typing import List, Optional

from sqlalchemy.orm import Session

from backends.database.sql import crud
from backends.database.session import get_db
from backends.apps import schemas

ROUTER = APIRouter(tags=["GET"])


@ROUTER.get("/task", response_model=List[schemas.TaskModel])
async def rest_get_tasks(db: Session = Depends(get_db),
                         completed: Optional[bool] = None, 
                         request: Request = None):
    
    res = await crud.get_tasks(db=db, completed=completed)
    
    return res


@ROUTER.get("/task/{task_id}", response_model=schemas.TaskModel)
async def rest_get_task(task_id, 
                         db: Session = Depends(get_db)):
    
    res = await crud.get_task(tid=task_id, db=db)
    
    return res