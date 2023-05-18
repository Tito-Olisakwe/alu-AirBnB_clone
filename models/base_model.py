#!/usr/bin/python3
from datetime import datetime
import uuid
import models
from models import storage

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = None

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                     # Convert the string value to a datetime object
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
            
        # If it's a new instance, add a call to the method new(self) on storage
        if not kwargs:
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
  
    def save(self):
        self.updated_at = datetime.now()
        # Call the save(self) method for the storage instance
        models.storage.save()
   
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        if self.updated_at is not None:
            obj_dict["updated_at"] = self.updated_at.isoformat()
        else:
            obj_dict.pop("updated_at", None) # Remove 'updated_at' key if it's None
        return obj_dict
