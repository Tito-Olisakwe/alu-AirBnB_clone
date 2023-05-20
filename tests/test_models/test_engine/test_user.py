import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        # Create an instance of User for testing
        self.user = User()

    def tearDown(self):
        # Clean up after each test method
        del self.user

    def test_user_attributes(self):
        # Test the initial attributes of User
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_to_dict(self):
        # Test the to_dict() method of User
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["email"], "")
        self.assertEqual(user_dict["password"], "")
        self.assertEqual(user_dict["first_name"], "")
        self.assertEqual(user_dict["last_name"], "")

    def test_user_str_representation(self):
        # Test the __str__() method of User
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)


if __name__ == "__main__":
    unittest.main()
