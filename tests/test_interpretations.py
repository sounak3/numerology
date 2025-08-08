import os
import sys
import unittest

# # For relative imports to work in Python 3.6
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))

from numerology import Pythagorean
from numerology import Chaldean
from numerology import Vedic

class TestFlatInterpretations(unittest.TestCase):
    @classmethod
    def start_app(cls, call_name, surname, dob):
        print("Starting...\n")
        pythagores_nums = Pythagorean(first_name=call_name, last_name=surname, birthdate=dob, verbose=False)
        chaldean_nums = Chaldean(first_name=call_name, last_name=surname, birthdate=dob, verbose=False)
        vedic_nums = Vedic(first_name=call_name, last_name=surname, birthdate=dob, verbose=False)

        print(pythagores_nums.get_all_details())
        print(chaldean_nums.get_all_details())
        print(vedic_nums.get_all_details())

    def test_with_sample_data(self):
        test_data = [
            # ("Alice", "Johnson", "1990-01-15"),
            # ("Bob Kumar", "Smith", "1985-05-20"),
            # ("Charlie", "Mc Brown", "1978-12-03"),
            ("Sounak", "Choudhury", "1983-07-20")
        ]

        for first_name, last_name, birthdate in test_data:
            with self.subTest(first_name=first_name, last_name=last_name, birthdate=birthdate):
                print(f"Testing with: {first_name} {last_name}, Birthdate: {birthdate}")
                self.start_app(first_name, last_name, birthdate)
                print("Test completed successfully.\n")

if __name__ == "__main__":
    unittest.main()
