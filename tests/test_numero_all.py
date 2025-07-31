import os
import sys
import unittest

# # For relative imports to work in Python 3.6
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from numerology import Pythagorean
from numerology import Chaldean
from numerology import Vedic

class TestStartApp(unittest.TestCase):
    @classmethod
    def start_app(cls, first_name, last_name, birthdate):
        print("Starting...\n")
        Pythagorean(first_name, last_name, birthdate)
        Chaldean(first_name, last_name, birthdate)
        Vedic(first_name, last_name, birthdate)

    def test_with_sample_data(self):
        test_data = [
            ("Alice", "Johnson", "1990-01-15"),
            ("Bob Kumar", "Smith", "1985-05-20"),
            ("Charlie", "Mc Brown", "1978-12-03")
        ]

        for first_name, last_name, birthdate in test_data:
            with self.subTest(first_name=first_name, last_name=last_name, birthdate=birthdate):
                print(f"Testing with: {first_name} {last_name}, Birthdate: {birthdate}")
                self.start_app(first_name, last_name, birthdate)
                print("Test completed successfully.\n")

if __name__ == "__main__":
    unittest.main()
