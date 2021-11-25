from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from backends.database.sql import crud
from backends.database.session import get_db
from backends.apps import schemas

from starlette.responses import JSONResponse

ROUTER = APIRouter(tags=["DELETE"])

@ROUTER.delete("/task/{task_id}", response_model=schemas.TaskModel)
async def rest_delete_task(task_id: int = None,
                         db: Session = Depends(get_db)):
    
    res = await crud.delete_task(tid=task_id, db=db)
    db.commit()

    return res

@ROUTER.delete("/task", response_model=schemas.TaskModel)
async def rest_delete_task(db: Session = Depends(get_db)):
    
    res = await crud.delete_tasks(db=db)
    db.commit()
    
    return res