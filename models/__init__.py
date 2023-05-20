#!/usr/bin/python3
"""The __init__ method for models directory"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Call reload() method on this variable
storage.reload()

classes = {"BaseModel": BaseModel}
