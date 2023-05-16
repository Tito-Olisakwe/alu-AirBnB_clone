#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id : str(uuid.uuid4())
        self.created_at : datetime.now()
        self.updated_at : self.created_at

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.update_at = datetime.now()
    
    def to_dict(self):
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict