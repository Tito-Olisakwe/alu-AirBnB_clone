#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

        if kwargs:
            kwargs.pop('__class__', None)
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            super().__init__(**kwargs)
        else:
            super().__init__()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Return a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        if self.updated_at is not None:
            obj_dict['updated_at'] = self.updated_at.isoformat()
        else:
            obj_dict['updated_at'] = None
        return obj_dict
