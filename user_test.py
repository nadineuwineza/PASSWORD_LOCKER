import unittest
from user import Users
from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = Users("Nadine", "nana")
    def test_init(self):
        self.assertEqual(self.new_user.username, "Nadine")
        self.assertEqual(self.new_user.password, "nana")

    def test_login(self):
        self.assertTrue(self.new_user.username, 'Nadine')
        self.assertTrue(self.new_user.password, 'nana')    

    def test_delete(self):
        self.assertTrue(self.new_user.username, 'Nadine')
        self.assertTrue(self.new_user.password, 'nana') 

    def test_create(self):
        self.assertTrue(self.new_user.username, 'Nadine')
        self.assertTrue(self.new_user.password, 'nana')  

if __name__ == '__main__':
    unittest.main()        