from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from backends.database.sql import crud
from backends.database.session import get_db
from backends.apps import schemas

ROUTER = APIRouter(tags=["POST"])

@ROUTER.post("/task", response_model=schemas.TaskModel)
async def rest_post_task(data: schemas.TaskModel,
                         db: Session = Depends(get_db)):
    
    res = await crud.post_task(data=data, db=db)
    db.commit()
    
    return res