#!/usr/bin/python3
"""
Test for the DBStorage
"""
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from models import storage


class TestDBStorageMethods(unittest.TestCase):
    """Test the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the DBStorage tests"""
        cls.state = State(name="California")
        storage.new(cls.state)
        storage.save()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database"""
        storage.delete(cls.state)
        storage.save()

    def test_get_method(self):
        """
        Test if the get method
        returns the correct object based on class and ID
        """
        retrieved_state = storage.get(State, self.state.id)
        self.assertEqual(retrieved_state.id, self.state.id)
        self.assertEqual(retrieved_state.name, "California")
        self.assertIsInstance(retrieved_state, State)


if __name__ == "__main__":
    unittest.main()
