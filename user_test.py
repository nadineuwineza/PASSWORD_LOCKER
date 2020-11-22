import unittest
from user import Users
from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = Users("Nadine", "nana")
    def test_init(self):
        self.assertEqual(self.new_user.username, "Nadine")
        self.assertEqual(self.new_user.password, "nana")