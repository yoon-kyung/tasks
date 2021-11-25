from typing import Optional
from pydantic import BaseModel
import datetime as dt

class TaskModel(BaseModel):
    
    id: int = None 
    created_at: dt.datetime = None
    updated_at: dt.datetime = None
    deleted_at: dt.datetime = None
    name: Optional[str] = None 
    completed: Optional[bool] = None        
    
    class Config:
        orm_mode = True
        
    def validate_task(self):
        if not self.name:
            raise ValueError("name은 반드시 입력해야 합니다.")
            