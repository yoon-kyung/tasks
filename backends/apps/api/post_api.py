from fastapi import Depends, APIRouter
from pydantic.networks import EmailStr

from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from backends.database.sql import crud
from backends.database.session import get_db
from backends.apps import schemas

from backends.loggers.loggers import basic_logger
logger = basic_logger("bo_report")

ROUTER = APIRouter(tags=["POST"])

@ROUTER.post("/task", response_model=schemas.TaskModel)
async def rest_post_task(data: schemas.TaskModel,
                         db: Session = Depends(get_db)):
    
    try:
        
        logger.info(f"{__name__}.py:::{data}")
        
        data.validate_task()
        
        res = await crud.post_task(data=data, db=db)
        db.commit()
    except Exception as e:
        logger.warning(f"{__name__}.py:::exception발생:::{e}")
        return JSONResponse(status_code=400, content=dict(msg=str(e)))
    
    return res