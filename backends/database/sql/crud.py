from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null

from backends.apps import schemas
from backends.database import models

from starlette.responses import JSONResponse


async def get_tasks(request = None, db: Session = None, kwlist: list = None):
    
    # GET 호출 시 deleted_at이 None이 아닌 것은 return 하지 않는다.
    tasks = db.query(models.Task).filter(models.Task.deleted_at == None).all()
    
    res = [schemas.TaskModel.from_orm(task) for task in tasks]
    if not res:
        return JSONResponse(status_code=404, content=dict(msg="데이터가 없습니다."))
    return res


async def get_task(tid: int, db: Session = None):
    
    # GET 호출 시 deleted_at이 None이 아닌 것은 return 하지 않는다.
    task = db.query(models.Task).filter(models.Task.id == tid,
                                        models.Task.deleted_at == None).first()
    if not task:
        return JSONResponse(status_code=404, content=dict(msg="데이터가 없습니다."))
    
    res = schemas.TaskModel.from_orm(task)
    return res


async def post_task(data, db: Session = None):
    
    # schema를 dictionary로 변경
    if type(data) != dict:
        data = dict(data)
    
    add_data = models.Task(**data)
    db.add(add_data)
    db.flush()
    
    res = schemas.TaskModel.from_orm(add_data)
    return res
    

async def patch_task(tid: int, data, db: Session = None):
    
    init = db.query(models.Task).filter(models.Task.id == tid).first()
    
    data_dict = data.dict()
    for k, v in data_dict.items():
        if v is None:
            continue
        setattr(init, k, v)
                
    db.flush()
    
    res = schemas.TaskModel.from_orm(init)
    return res


async def delete_tasks(db: Session = None):
    init = db.query(models.Task).filter(models.Task.deleted_at == None).all()
    for i in init:
        i.deleted_at = datetime.now()
    
    db.flush()
    
    return JSONResponse(status_code=200, content=dict(msg=f"삭제된 게시글은 총 {len(init)}개 입니다."))
    
    
async def delete_task(tid: int, db: Session = None):
    
    init = db.query(models.Task).filter(models.Task.id == tid).first()
    if init.deleted_at:
        return JSONResponse(status_code=404, content=dict(msg="이미 삭제된 게시글입니다."))
    init.deleted_at = datetime.now()
                
    db.flush()
    
    res = schemas.TaskModel.from_orm(init)
    return res
    
    