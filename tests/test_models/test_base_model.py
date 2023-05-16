import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        """Test the attributes of the BaseModel class"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsNone(bm.updated_at)

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        bm = BaseModel()
        expected_outcome = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_outcome)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        if bm.updated_at is not None:
            self.assertEqual(bm_dict['updated_at'], bm.updated_at.isoformat())
            