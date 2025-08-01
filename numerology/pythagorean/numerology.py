import gettext
import logging
import math
import os
import locale
import sys
from collections import Counter
from typing import Dict, Optional, Tuple

from .common import Functions as fct
from .interpretations import Interpretations

localedir_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "locale"
)

default_lang = "en"
try:
    locale_lang, encoding = locale.getlocale()
    lang = locale_lang.split("_")[0] if locale_lang else default_lang
except Exception:
    # If unable to get the locale language, use English
    lang = default_lang
try:
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[lang]
    )
except Exception:
    # If the current language does not have a translation, the default language (English) will be used English
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[default_lang]
    )
language.install()
_ = language.gettext


class Numerology:
    """Numerology is the science of numbers. It is the study of the numerical value of the letters in words, names, dates, and ideas.

    Pythagoras, the Greek mathematician and philosopher who lived from 569–470 B.C.,
    began his theory of numbers by discovering the numerical relationship between numbers and musical notes.

    Then he studied numerology from Egyptians priests and is now known as the father of Western numerology.

    This class is mainly based on the calculation methods from the book "ABC de la Numérologie" of Jean-Daniel FERMIER.
    """

    alphabet = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 1,
        "k": 2,
        "l": 3,
        "m": 4,
        "n": 5,
        "o": 6,
        "p": 7,
        "q": 8,
        "r": 9,
        "s": 1,
        "t": 2,
        "u": 3,
        "v": 4,
        "w": 5,
        "x": 6,
        "y": 7,
        "z": 8,
    }

    vowels = ("a", "e", "i", "o", "u", "y")

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
        "z",
    )

    _key_figures = {}

    first_name: str
    last_name: str
    birthdate: Optional[str]

    first_name_num: Tuple[int]
    last_name_num: Tuple[int]

    first_name_is_valid: bool = False
    last_name_is_valid: bool = False
    birthdate_is_valid: bool = False
    names_are_valid: bool = False

    verbose = True

    def __init__(
        self,
        first_name: str,
        last_name: str,
        birthdate: Optional[str] = None,
        verbose: bool = True,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.verbose = verbose

        self.check_parameters()
        if self.names_are_valid:
            self.init_inner_variables()
            self.set_key_figures()
            self._interpretations = Interpretations(key_figures=self.key_figures)

        if self.verbose and self.names_are_valid:
            print(_("KEY FIGURES:"))
            fct.print_beautiful_dict(dictionary=self.key_figures)
            print(_("INTERPRETATIONS:"))
            fct.print_beautiful_dict(dictionary=self.interpretations)

    # CLASSMETHODS

    @classmethod
    def get_numerology_sum(
        cls, tuple_obj: Tuple[int, ...], upper_bound: int = 9, master_number: bool = True
    ) -> int:
        """Make the numerology sum of the iterable (here, tuples) in parameter.
        The numerology sum is the sum of every digit in a number.
        The result is sum again if it is greater than 9 unless it's a multiple of 11.

        Args:
            tuple_obj (Tuple[int]): Tuple to sum up
            upper_bound (int, optional): Upper bound of the recursive. Defaults to 9.
            master_number (bool, optional): If `master_number` is False, the multiple of 11 are not taken into account. Defaults to True.

        Returns:
            int: [description]
        """
        nsum = math.fsum(tuple_obj)

        if master_number:
            while not (nsum <= upper_bound or (nsum % 11) == 0):
                nsum = math.fsum(tuple(int(num) for num in str(int(nsum))))
        else:
            while not (nsum <= upper_bound):
                nsum = math.fsum(tuple(int(num) for num in str(int(nsum))))

        return int(nsum)

    # INIT METHODS

    def get_key_figures(self):
        if self.names_are_valid:
            self.init_inner_variables()
            self.set_key_figures()
            self._interpretations = Interpretations(key_figures=self.key_figures)
            return self.key_figures
        else:
            return 'None'

    def check_parameters(self):
        self.check_first_name()
        self.check_last_name()

        if self.first_name_is_valid and self.last_name_is_valid:
            self.names_are_valid = True
            self.check_birthdate()
        else:
            logging.warning("Invalid names supplied.")
            print(_("Invalid names supplied."))

    def check_first_name(self):
        """Check if the first name supplied contains at least one letter of the alphabet."""
        if fct.keep_valid_letters(self.first_name, self.alphabet):
            self.first_name_is_valid = True

    def check_last_name(self):
        """Check if the last name supplied contains at least one letter of the alphabet."""
        if fct.keep_valid_letters(self.last_name, self.alphabet):
            self.last_name_is_valid = True

    def check_birthdate(self):
        """Check if the birthdate supplied is a valid date."""
        if self.birthdate and fct.is_valid_date(self.birthdate):
            self.birthdate_is_valid = True

    def init_inner_variables(self):
        """Initializes the inner variables of the class as cleaned version of names, etc."""
        # first_name is the first name as supplied by the user.
        # first_name_cleaned is the clean version of the first_name : lower case, accents removed, only alphabet letters kept.
        # first_name_num is the matching numbers of first_name_cleaned.
        # Same for last_name.

        # Initialize the variables - Set the names and birthdate and their matching numbers.
        self.first_name_cleaned = fct.keep_valid_letters(self.first_name, self.alphabet)
        self.last_name_cleaned = fct.keep_valid_letters(self.last_name, self.alphabet)

        self.first_name_num = fct.match_numbers_to_letters(self.first_name_cleaned, self.alphabet)
        self.last_name_num = fct.match_numbers_to_letters(self.last_name_cleaned, self.alphabet)

        if self.birthdate_is_valid and self.birthdate is not None:
            self.birthdate_year = int(self.birthdate.split("-")[0])
            self.birthdate_month = int(self.birthdate.split("-")[1])
            self.birthdate_day = int(self.birthdate.split("-")[2])

    def set_key_figures(self):
        """Initializes the key figures dictionary."""

        # First name and last name elements
        if self.names_are_valid:
            # Setting the key figures
            self._key_figures["first_name"] = self.first_name
            self._key_figures["last_name"] = self.last_name
            # Hearts Desire Number (vowels) = Nombre intime (voyelles)
            self._key_figures["hearts_desire_number"] = self.hearts_desire_number
            # Personality Number (consonants) = Nombre de réalisation (consonnes)
            self._key_figures["personality_number"] = self.personality_number
            # Destiny Number (full name) = Nombre d'expression (nom complet)
            self._key_figures["destiny_number"] = self.destiny_number
            self._key_figures["expression_number"] = self.destiny_number
            # Active Number (first name) = Nombre actif (prénom)
            self._key_figures["active_number"] = self.active_number
            # Legacy Number (last name) = Nombre héréditaire (nom de famille)
            self._key_figures["legacy_number"] = self.legacy_number
            self._key_figures["full_name_numbers"] = self.full_name_numbers
            self._key_figures[
                "full_name_missing_numbers"
            ] = self.full_name_missing_numbers
            self._key_figures["name_number"] = None
            self._key_figures["psychic_number"] = None

        # Birthdate elements (as birthdate is optional)
        if self.birthdate_is_valid:
            self._key_figures["birthdate"] = self.birthdate
            self._key_figures["life_path_number"] = self.life_path_number
            self._key_figures[
                "life_path_number_alternative"
            ] = self.life_path_number_alternative
            self._key_figures["birthdate_day_num"] = self.birthdate_day_num
            self._key_figures["birthdate_month_num"] = self.birthdate_month_num
            self._key_figures["birthdate_year_num"] = self.birthdate_year_num
            self._key_figures[
                "birthdate_year_num_alternative"
            ] = self.birthdate_year_num_alternative
            self._key_figures["attitude_number"] = self.attitude_number
            self._key_figures["karma_number"] = self.karma_number
            self._key_figures["karmic_debt_numbers"] = self.karmic_debt_numbers
            self._key_figures["power_number"] = self.power_number
            self._key_figures[
                "power_number_alternative"
            ] = self.power_number_alternative

    # PROPERTIES
    @property
    def key_figures(self) -> Dict[str, int]:
        """Returns the keys figures in a dictionary."""
        return self._key_figures

    @property
    def interpretations(self) -> Dict:
        return self._interpretations.meanings

    @property
    def life_path_number(self) -> tuple:
        """Returns the Life Path Number.

        The life path number, also referred as Lucky Number in some places, is the most important one in a numerology chart.
        It describes the direction of your life journey.
        It offers insight into the skills and traits you may possess and the kinds of challenges you can expect to face in your life.
        It is calculated from the birth date.

        This method sums-reduces to one digit the date, month, and year before summing-reducing their total.
        The alternative method `life_path_number_alternative` sums-reduces to one digit the total of day, month, and year from the birthdate.

        Returns:
            int: Life Path Number (Initial method).
        """
        if self.birthdate:
            day = self.get_numerology_sum(
                fct.int_to_tuple(self.birthdate_day), master_number=False
            )
            month = self.get_numerology_sum(
                fct.int_to_tuple(self.birthdate_month), master_number=False
            )
            year = self.get_numerology_sum(
                fct.int_to_tuple(self.birthdate_year), master_number=False
            )
            nsum = day + month + year
            return (self.get_numerology_sum(fct.int_to_tuple(nsum), master_number=False),)
        else:
            print("WARNING: Birthdate is not set. Cannot calculate Life Path Number.")
            return (0,)

    @property
    def life_path_number_alternative(self) -> tuple:
        """Returns the Life Path Number (alternative method).

        The life path number is the most important one in a numerology chart.
        It describes the direction of your life journey.
        It offers insight into the skills and traits you may possess and the kinds of challenges you can expect to face in your life.
        It is calculated from the birth date.

        The initial method sums-reduces to one digit the date, month, and year before summing-reducing their total.
        This alternative method `life_path_number_alternative` sums-reduces to one digit the total of day, month, and year from the birthdate.

        Returns:
            int: Life Path Number (Alternative method)
        """
        nsum = self.birthdate_day + self.birthdate_month + self.birthdate_year
        return (self.get_numerology_sum(fct.int_to_tuple(nsum), master_number=False),)

    @property
    def destiny_number(self) -> tuple:
        """Returns the Destiny Number.

        Sometimes called Expression Number or Lucky Number, it indicates the personal interest, unique capabilities and talents.

        Returns:
            int: Destiny number.
        """
        active_number = self.get_numerology_sum(
            self.first_name_num, master_number=False
        )
        legacy_number = self.get_numerology_sum(self.last_name_num, master_number=False)
        return (self.get_numerology_sum((active_number, legacy_number), master_number=True),)

    @property
    def power_number(self) -> tuple:
        """Returns the Power Number

        Sometimes called the Maturity Number, the power number is obtained by adding together the life path number and destiny number. Then reduce the number to a single digit.

        Returns:
            int: [description]
        """
        return (self.get_numerology_sum(fct.int_to_tuple(self.life_path_number[0] + self.destiny_number[0]),
            master_number=False),)

    @property
    def power_number_alternative(self) -> tuple:
        """Returns the Power Number (Alternative)

        Sometimes called the Maturity Number, the power number is obtained by adding together the life path number (alternative) and destiny number. Then reduce the number to a single digit.

        Returns:
            int: [description]
        """
        return (self.get_numerology_sum(fct.int_to_tuple(self.life_path_number_alternative[0] + self.destiny_number[0]),
            master_number=False),)

    @property
    def personality_number(self) -> int:
        """Returns the Personality Number.

        Sometimes called the Inner Dream or Personal Dream Number, the Personality Number indicates our external personality.
        It is calculated from the consonants in the full name.

        Returns:
            int: Inner Dream Number.
        """
        consonants_in_name_num = fct.match_numbers_to_letters(
            ''.join(
                letter
                for letter in (self.first_name_cleaned + self.last_name_cleaned)
                if letter in self.consonants
            ),
            self.alphabet
        )
        return self.get_numerology_sum(consonants_in_name_num)

    @property
    def hearts_desire_number(self) -> int:
        """Returns the Hearts Desire Number.

        Sometimes called the Soul Urge or Soul Prompting Number, the Hearts Desire Number describes the inner desires.
        It is calculated from the vowels in the full name.

        Returns:
            int: Hearts Desire Number.
        """
        vowels_in_name_num = fct.match_numbers_to_letters(
            ''.join(
                letter
                for letter in (self.first_name_cleaned + self.last_name_cleaned)
                if letter in self.vowels
            ),
            self.alphabet
        )
        return self.get_numerology_sum(vowels_in_name_num)

    @property
    def active_number(self) -> Tuple[int]:
        """Returns the Active Number.

        The number from your first name.

        Returns:
            int: The Active Number
        """
        return (self.get_numerology_sum(self.first_name_num, master_number=False),)

    @property
    def legacy_number(self) -> Tuple[int]:
        """Returns the Legacy Number.

        The number from your last name.

        Returns:
            int: The legacy number
        """
        return (self.get_numerology_sum(self.last_name_num, master_number=False),)

    @property
    def full_name_numbers(self) -> Dict[int, int]:
        """Returns the numbers from the full name as a dict(Counter).

        The dict contains the numbers and their occurrences."""
        full_name = self.first_name_cleaned + self.last_name_cleaned
        full_name_num = fct.match_numbers_to_letters(full_name, self.alphabet)
        full_name_counter = Counter(full_name_num).most_common()
        full_name_counter_dict = dict(full_name_counter)
        return full_name_counter_dict

    @property
    def full_name_missing_numbers(self) -> Tuple:
        """Returns the missing numbers from the name as a tuple.
        
        Also called Karmic lesson numbers, shows a vacuum that needs to be filled in this lifetime by mastering the required Karmic lesson."""
        full_name = self.first_name_cleaned + self.last_name_cleaned
        full_name_num = fct.match_numbers_to_letters(full_name, self.alphabet)
        return tuple([number for number in range(1, 10) if number not in full_name_num])

    @property
    def birthdate_day_num(self) -> Tuple[int]:
        """Returns the numerology sum of the birthday day.

        Example: The 27 in 1986-03-27 will give 9."""
        return (self.get_numerology_sum(fct.int_to_tuple(self.birthdate_day), master_number=False),)

    @property
    def birthdate_month_num(self) -> int:
        """Returns the numerology sum of the birthday month.

        Example: The 12 in 1986-12-27 will give 3."""
        return self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_month), master_number=False
        )

    @property
    def birthdate_year_num(self) -> int:
        """Returns the numerology sum of the birthday year.

        This method sums-reduces the 4 digits of the year.
        The alternative one sums-reduces the 2 last digits."""
        return self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_year), master_number=False
        )

    @property
    def birthdate_year_num_alternative(self) -> int:
        """Returns the numerology sum of the birthday year.

        The original method sums-reduces the 4 digits of the year (1958 > 23 > 5).
        This alternative one sums-reduces the 2 last digits ((19)58 > 13 > 4)."""
        birthday_year_truncate = int(str(self.birthdate_year)[-2:])
        return self.get_numerology_sum(
            fct.int_to_tuple(birthday_year_truncate), master_number=False
        )

    @property
    def attitude_number(self) -> int:
        """Returns the numerology sum of the birthday date and month.

        Sometimes called the Sun Number, the Attitude Number indicates how we behave in situations with others Or our attitude towards them.
        Example: The sum of 27th of December in 1986-12-27 will 27+12 > 12 > 3."""
        if self.birthdate:
            day = self.get_numerology_sum(
                fct.int_to_tuple(self.birthdate_day), master_number=False
            )
            month = self.get_numerology_sum(
                fct.int_to_tuple(self.birthdate_month), master_number=False
            )
            nsum = day + month
            return self.get_numerology_sum(fct.int_to_tuple(nsum), master_number=False)
        return 0

    @property
    def karma_number(self) -> int:
        """Returns the numerology sum of the (birthday date - 1).

        Example: For 1986-12-27 will be 27-1 > 26 > 8."""
        if self.birthdate:
            day = self.birthdate_day - 1
            return self.get_numerology_sum(fct.int_to_tuple(day), master_number=False)
        return 0

    @property
    def karmic_debt_numbers(self) -> Dict[str, int]:
        """Returns Karmic debts associated with any of Life Path, Personality, Birth Day, Expression, and Heart’s Desire."""
        debt_numbers = [19, 13, 14, 16]
        core_karmic_num = {}
        day = fct.int_to_tuple(self.birthdate_day)
        month = fct.int_to_tuple(self.birthdate_month)
        year = fct.int_to_tuple(self.birthdate_year)
        nsum = day + month + year
        life_path_number = self.get_numerology_sum(nsum, upper_bound=19, master_number=False)
        if life_path_number in core_karmic_num:
            core_karmic_num["life_path_number"] = life_path_number

        vowels_in_name_num = fct.match_numbers_to_letters(
            ''.join(
                letter
                for letter in (self.first_name_cleaned + self.last_name_cleaned)
                if letter in self.vowels
            ),
            self.alphabet
        )
        hearts_desire_number = self.get_numerology_sum(vowels_in_name_num, upper_bound=19)
        if hearts_desire_number in debt_numbers:
            core_karmic_num["hearts_desire_number"] = hearts_desire_number

        consonants_in_name_num = fct.match_numbers_to_letters(
            ''.join(
                letter
                for letter in (self.first_name_cleaned + self.last_name_cleaned)
                if letter in self.consonants
            ),
            self.alphabet
        )
        personality_number = self.get_numerology_sum(consonants_in_name_num, upper_bound=19)
        if personality_number in debt_numbers:
            core_karmic_num["personality_number"] = personality_number

        destiny_number = self.get_numerology_sum(
            (self.active_number[0], self.legacy_number[0]), upper_bound=19, master_number=True
        )
        if destiny_number in debt_numbers:
            core_karmic_num["destiny_number"] = destiny_number

        birthdate_day_num = self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_day), upper_bound=19, master_number=False
        )
        if birthdate_day_num in debt_numbers:
            core_karmic_num["birthdate_day_num"] = birthdate_day_num

        return core_karmic_num

