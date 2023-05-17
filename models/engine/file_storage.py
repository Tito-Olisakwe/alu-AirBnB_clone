#!/usr/bin/python3
import json

"""This module is responsible for managing the serialization,
and deserialization of objects to and from a JSON file."""

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
        with open(self.__file_path, 'w') as file:
            data = {}
            for key, value in self.__objects.items():
                data[key] = value.to_dict()
                json.dump(data, file)

    def reload(self):
        """deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
