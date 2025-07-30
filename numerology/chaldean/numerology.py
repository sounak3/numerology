import os
import locale
import gettext
from numerology.pythagorean import *
import pythagorean.numerology as pNumerology

from pythagorean.common import Functions as fct
from chaldean.interpretations import Interpretations as CInterpretations

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

class CNumerology(pNumerology.Numerology):
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
        super().__init__(first_name, last_name, birthdate, False)
        self.verbose = verbose
        if self.names_are_valid:
            self._interpretations = CInterpretations(key_figures=self.key_figures)
        if self.verbose and self.names_are_valid:
            print(_("KEY FIGURES:"))
            fct.print_beautiful_dict(dictionary=self.key_figures)
            print(_("INTERPRETATIONS:"))
            fct.print_beautiful_dict(dictionary=self.interpretations)

    def set_key_figures(self):
        """Initializes the key figures dictionary."""
        self._key_figures["life_path_number"] = self.life_path_number
        self._key_figures["birthdate_day_num"] = self.birthdate_day_num
        self._key_figures["birthdate_year_num_alternative"] = self.birthdate_year_num_alternative
        self._key_figures["name_number"] = self.name_number
        self._key_figures["active_number"] = self.active_number
        self._key_figures["life_path_number_alternative"] = None
        self._key_figures["destiny_number"] = None
        self._key_figures["expression_number"] = None
        self._key_figures["psychic_number"] = None
        self._key_figures["attitude_number"] = None
        self._key_figures["karma_number"] = None
        self._key_figures["karmic_debt_numbers"] = None
        self._key_figures["power_number"] = None
        self._key_figures["power_number_alternative"] = None
        self._key_figures["full_name_numbers"] = None
        self._key_figures["full_name_missing_numbers"] = None

    @property
    def name_number(self) -> tuple:
        """Returns the Name Number.

        Name Numbers, also known as Spiritual Numbers, denote the inner you, as well as any hidden influences that play a role in your life (present and future).
        It is calculated from adding the numbers assigned to the letters of your name full name. Then reduce till double digits.

        Returns:
            tuple: Name Number.
        """
        active_number = self.get_numerology_sum(self.first_name_num, master_number=False)
        legacy_number = self.get_numerology_sum(self.last_name_num, master_number=False)
        nsum = active_number + legacy_number
        if (nsum,) == self.destiny_number:
            return self.destiny_number
        else:
            return (nsum,), self.destiny_number

    @property
    def birthdate_year_num_alternative(self) -> int:
        """Returns the numerology sum of the birthday year.

        This method sums-reduces the 4 digits of the year.
        This alternative one reduces upto 2 digits till 52."""
        return self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_year), upper_bound=52, master_number=True
        )

    @property
    def active_number(self) -> tuple:
        """Returns the First Name / Active Number.

        The numbers from your first name.

        Returns:
            tuple: The Active Number
        """
        first_name_compound = self.get_numerology_sum(self.first_name_num, upper_bound=52, master_number=True)
        first_name_single   = self.get_numerology_sum(self.first_name_num, master_number=False)
        if first_name_compound == first_name_single:
            return (first_name_single,)
        else:
            return first_name_compound, first_name_single

    @property
    def birthdate_day_num(self) -> tuple:
        """Returns the numerology sum of the birthday day.

        Example: The 27 in 1986-03-27 will give 27,9."""
        birthdate_day_single = self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_day), master_number=False
        )
        if self.birthdate_day == birthdate_day_single:
            return (birthdate_day_single,)
        else:
            return self.birthdate_day, birthdate_day_single

    @property
    def life_path_number(self) -> tuple:
        """Returns the Life Path Number Or Birthdate Number.

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
            num_sum = self.get_numerology_sum(fct.int_to_tuple(nsum), master_number=False)
            if nsum == num_sum:
                return (num_sum,)
            else:
                return nsum, num_sum
        else:
            print(f"{Colors.WARNING}Birthdate is not set. Cannot calculate Life Path Number.{Colors.ENDC}")
            return (0,)
