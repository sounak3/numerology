from numerology import Pythagorean
from numerology import Chaldean
from numerology import Vedic
import argparse

def start_app(first_name, last_name, birthdate):
    print("Starting...\n")
    Pythagorean(first_name, last_name, birthdate)
    Chaldean(first_name, last_name, birthdate)
    Vedic(first_name, last_name, birthdate)

if __name__ == "__main__":
    """Interactive version of the package."""
    parser = argparse.ArgumentParser(description="Run numerology calculations")
    parser.add_argument("--first_name", help="Your first name")
    parser.add_argument("--last_name", help="Your last name")
    parser.add_argument("--birthdate", help="Birthdate in YYYY-MM-DD format")
    args = parser.parse_args()

    # Prompt for any missing arguments
    first_name = args.first_name or input("Enter your first name: ")
    last_name = args.last_name or input("Enter your last name: ")
    birthdate = args.birthdate or input("Enter your birthdate (yyyy-MM-dd, example 1994-11-30): ")

    start_app(first_name, last_name, birthdate)