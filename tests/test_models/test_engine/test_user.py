import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test User class."""

    def test_instance(self):
        """test instance."""
        user = User()
        self.assertIsInstance(user, User)

    def test_is_class(self):
        """test is a class type."""
        user = User()
        self.assertEqual(str(type(user)),
                         "<class 'models.user.User'>")

    def test_is_subclass(self):
        """test is_subclass."""
        user = User()
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_id(self):
        """test email."""
        user = User()
        self.assertIsNotNone(user.id)

    def test_email(self):
        """test email."""
        user = User()
        self.assertEqual(user.email, "")
        user.email = "airbnb@mail.com"
        self.assertEqual(user.email, "airbnb@mail.com")

    def test_password(self):
        """test password."""
        user = User()
        self.assertEqual(user.password, "")
        user.password = "root"
        self.assertEqual(user.password, "root")

    def test_first_name(self):
        """test first name."""
        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "Betty"
        self.assertEqual(user.first_name, "Betty")

    def test_last_name(self):
        """test last name."""
        user = User()
        self.assertEqual(user.last_name, "")
        user.first_name = "Bar"
        self.assertEqual(user.first_name, "Bar")


if __name__ == "__main__":
    unittest.main()