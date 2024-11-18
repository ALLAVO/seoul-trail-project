# test_api.py
import unittest
from app.utils import fetch_trail_data

class TestAPI(unittest.TestCase):
    def test_fetch_trail_data(self):
        data = fetch_trail_data(1, 5)
        self.assertIsNotNone(data)

if __name__ == "__main__":
    unittest.main()
