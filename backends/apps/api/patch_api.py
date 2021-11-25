from fastapi import Depends, APIRouter

from sqlalchemy.orm import Session

from backends.database.sql import crud
from backends.database.session import get_db
from backends.apps import schemas

from starlette.responses import JSONResponse

from backends.loggers.loggers import basic_logger
logger = basic_logger("bo_report")


ROUTER = APIRouter(tags=["PATCH"])

@ROUTER.patch("/task/{task_id}", response_model=schemas.TaskModel)
async def rest_patch_task(task_id,
                         data: schemas.TaskModel,
                         db: Session = Depends(get_db)):
    
    try:
        data.validate_task()
        
        logger.info(f"{__name__}.py:::{data}")
    
        res = await crud.patch_task(tid=task_id, data=data, db=db)
        db.commit()

    except Exception as e:
        return JSONResponse(status_code=400, content=dict(msg=str(e)))
    
    return res