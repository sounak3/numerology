from typing import Optional
from numerology.pythagorean import *
import pythagorean.numerology as pnumerology

from pythagorean.common import Functions as fct
from .interpretations import Interpretations

class CNumerology(pnumerology.Numerology):
    """Numerology is the science of numbers. It is the study of the numerical value of the letters in words, names, dates, and ideas.

    The Chaldean numerology system is perhaps the oldest form of numerology known, with its origin in ancient Babylon.
    Chaldean system used sounds and tones to correspond letters and numbers. The Chaldean style matches the vibrations between the two.

    This class is mainly based on the calculation methods from the book "Palmistry Numerology and Astrology" of Cheiro.
    """

    alphabet = {
                'a': 1,
                'b': 2,
                'c': 3,
                'd': 4,
                'e': 5,
                'f': 8,
                'g': 3,
                'h': 5,
                'i': 1,
                'j': 1,
                'k': 2,
                'l': 3,
                'm': 4,
                'n': 5,
                'o': 7,
                'p': 9,
                'q': 1,
                'r': 2,
                's': 3,
                't': 4,
                'u': 6,
                'v': 6,
                'w': 6,
                'x': 5,
                'y': 1,
                'z': 7
            }

    vowels = ("a", "e", "i", "o", "u")

    consonants = (
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    )

    def __init__(self, first_name: str, last_name: str, birthdate: str, verbose: bool = True):
        super().__init__(first_name, last_name, birthdate, verbose)
        if self.names_are_valid:
            self._interpretations = Interpretations(key_figures=self.key_figures)

    def set_key_figures(self):
        """Initializes the key figures dictionary."""
        super().set_key_figures()
        self._key_figures["compound_number"] = self.compound_number
        self._key_figures["name_number"] = None
        self._key_figures["destiny_number"] = None
        self._key_figures["psychic_number"] = None
        self._key_figures["attitude_number"] = None
        self._key_figures["karma_number"] = None
        self._key_figures["karmic_debt_numbers"] = None
        self._key_figures["power_number"] = None
        self._key_figures["power_number_alternative"] = None
        self._key_figures["full_name_numbers"] = None
        self._key_figures["full_name_missing_numbers"] = None

    @property
    def compound_number(self) -> int:
        """Returns the Compound Number.

        Compound Numbers, also known as Spiritual Numbers, denote the inner you, as well as any hidden influences that play a role in your life (present and future).
        It is calculated from adding the numbers assigned to the letters of your name full name. Then reduce till double digits.

        Returns:
            int: Compound Number.
        """
        active_number = self.get_numerology_sum(self.first_name_num, master_number=False)
        legacy_number = self.get_numerology_sum(self.last_name_num, master_number=False)
        return active_number + legacy_number

    @property
    def birthdate_year_num_alternative(self) -> int:
        """Returns the numerology sum of the birthday year.

        This method sums-reduces the 4 digits of the year.
        This alternative one reduces upto 2 digits till 52."""
        return self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_year), upper_bound=52, master_number=True
        )
