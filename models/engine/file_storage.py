#!/usr/bin/python3
"""This module is responsible for managing the serialization,
and deserialization of objects to and from a JSON file."""

import json
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializez __objects to the JSON file (path: __file_path)."""
        data = {}
        for key, value in self.__objects.items():
            if hasattr(value, "to_dict"):
                data[key] = value.to_dict()
            else:
                data[key] = value.__dict__()

        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    if class_name == "BaseModel":
                        from models.base_model import BaseModel
                        cls = BaseModel

                    elif class_name == "User":
                        cls = User

                    elif class_name == "Place":
                        cls = Place

                    elif class_name == "State":
                        cls = State

                    elif class_name == "City":
                        cls = City

                    elif class_name == "Amenity":
                        cls = Amenity

                    elif class_name == "Review":
                        cls = Review

                    else:
                        cls = globals()[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
