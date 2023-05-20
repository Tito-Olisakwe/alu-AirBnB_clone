import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        """Test the attributes of the BaseModel class"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str(self):
        """Test the __str__ method of the BaseModel class"""
        bm = BaseModel()
        expected_outcome = "[{}] ({}) {}".format(bm.__class__.__name__, bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_outcome)

    def test_save(self):
        """Test the save method of the BaseModel class"""
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)
    
    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


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

    def test_from_dict(self):
        """Test creating a BaseModel instance from a dictionary"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        new_bm = BaseModel(**bm_dict)
        self.assertEqual(new_bm.id, bm.id)
        self.assertEqual(new_bm.created_at, bm.created_at)
        self.assertEqual(new_bm.updated_at, bm.updated_at)
        self.assertEqual(new_bm.__class__.__name__, bm.__class__.__name__)
        self.assertEqual(new_bm.__dict__, bm.__dict__)
        self.assertIsNot(new_bm, bm)  # Check that they are different instances

if __name__ == '__main__':
    unittest.main()
