from typing import Optional
from pydantic import BaseModel, validator
import datetime as dt

from starlette.responses import JSONResponse

class TaskModel(BaseModel):
    
    id: int = None 
    created_at: dt.datetime = None
    updated_at: dt.datetime = None
    deleted_at: dt.datetime = None
    name: str 
    completed: Optional[bool] = None        
    
    class Config:
        orm_mode = True
        
    def validate_task(self):
        if not self.name:
            raise ValueError("name은 반드시 입력해야 합니다.")
            