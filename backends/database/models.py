from sqlalchemy.sql.expression import false, null
from backends.database.session import Base
from sqlalchemy import Column, Integer, Text, Boolean, DateTime
import datetime


class Task(Base):
    
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    
    created_at = Column(DateTime, 
                        default=datetime.datetime.utcnow,
                        nullable=True)
    updated_at = Column(DateTime, 
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow,
                        nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    
    name = Column(Text, nullable=False)
    completed = Column(Boolean, default=false)