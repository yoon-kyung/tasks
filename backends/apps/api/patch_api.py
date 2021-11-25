from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from backends.database.sql import crud
from backends.database.session import get_db
from backends.apps import schemas

ROUTER = APIRouter(tags=["PATCH"])

@ROUTER.patch("/task/{task_id}", response_model=schemas.TaskModel)
async def rest_patch_task(task_id,
                         data: schemas.TaskModel,
                         db: Session = Depends(get_db)):
    
    res = await crud.patch_task(tid=task_id, data=data, db=db)
    db.commit()
    
    return res