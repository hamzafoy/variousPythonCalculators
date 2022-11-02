import unittest
from unittestclass import Phonebook

class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Hamza", "5029308392")
        number = phonebook.lookup("Hamza")
        self.assertEqual("5029308391", number)