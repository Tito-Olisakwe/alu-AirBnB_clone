import unittest
import os
import json
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.base_model = BaseModel()
    
    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
    
    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})
    
    def test_new(self):
        self.storage.new(self.base_model)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(self.base_model.id), all_objects)
        self.assertEqual(all_objects["BaseModel.{}".format(self.base_model.id)], self.base_model)
    
    def test_save_and_reload(self):
        models.storage.new(self.base_model)
        models.storage.save()
        models.storage.reload()

        obj = FileStorage._FileStorage__objects = {}
        
        self.assertIn("BaseModel.{}".format(self.base_model.id), obj)
    
    def test_save_file_exists(self):
        # Create an existing file
        with open(self.file_path, "w") as file:
            file.write("existing file")
        
        self.storage.new(self.base_model)
        self.storage.save()
        
        with open(self.file_path, "r") as file:
            data = json.load(file)
        
        self.assertIn("BaseModel.{}".format(self.base_model.id), data)
    
    def test_save_file_not_exists(self):
        self.storage.new(self.base_model)
        self.storage.save()
        
        self.assertTrue(os.path.exists(self.file_path))
    
    def test_reload_file_exists(self):
        # Create a file with invalid JSON data
        with open(self.file_path, "w") as file:
            file.write("invalid json")
        
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})
    
    def test_reload_file_not_exists(self):
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

if __name__ == "__main__":
    unittest.main()
