from pydantic import BaseModel, validator
import datetime as dt

class TaskModel(BaseModel):
    
    id: int = None 
    created_at: dt.datetime = None
    updated_at: dt.datetime = None
    deleted_at: dt.datetime = None
    name: str = None 
    completed: bool = None
            
    class Config:
        orm_mode = True