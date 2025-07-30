import gettext
import locale
import os
import sys
from typing import Dict, List, Optional

from .meanings import *

localedir_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "locale"
)

default_lang = "en"
try:
    locale_lang, encoding = locale.getlocale()
    lang = locale_lang.split("_")[0] if locale_lang else default_lang
except:
    # If unable to get the locale language, use English
    lang = default_lang
try:
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[lang]
    )
except:
    # If the current language does not have a translation, the default language (English) will be used English
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[default_lang]
    )
language.install()
_ = language.gettext


class Interpretations:

    key_figures: Dict = {}
    _meanings: Dict = {}

    def __init__(self, key_figures: Dict):
        self.key_figures = key_figures
        self.get_all_interpretations()

    def get_all_interpretations(self):
        for k, v in self.key_figures.items():
            self._meanings[k] = self.get_interpretation(k, v)

    @classmethod
    def get_interpretation(cls, name: str, value):
        interpretation = None

        if isinstance(value, str) and value.isdigit():
            num_value = int(value)
        elif isinstance(value, str):
            num_value = 0
        elif isinstance(value, int):
            num_value = value
        elif isinstance(value, (list, tuple)):
            num_value = int(''.join(map(str, value)) or 0)
        else:
            num_value = 0

        if name == "first_name":
            interpretation = value
        elif name == "last_name":
            interpretation = value
        elif name == "birthdate":
            interpretation = value
        elif name == "life_path_number":
            interpretation = {
                "name": _("Life Path Number"),
                "number": value,
                "meaning": cls.life_path_number(number=num_value),
            }
        elif name == "life_path_number_alternative":
            interpretation = {
                "name": _("Life Path Number Alternative"),
                "number": value,
                "meaning": cls.life_path_number(number=num_value),
            }
        elif name == "hearts_desire_number":
            interpretation = {
                "name": _("Hearts Desire (Soul urge) Number"),
                "number": value,
                "meaning": cls.hearts_desire_number(number=num_value),
            }
        elif name == "personality_number":
            interpretation = {
                "name": _("Personality Number"),
                "number": value,
                "meaning": cls.personality_number(number=num_value),
            }
        elif name == "destiny_number":
            interpretation = {
                "name": _("Destiny Number"),
                "number": value,
                "meaning": cls.destiny_number(number=num_value),
            }
        elif name == "expression_number":
            interpretation = {
                "name": _("Expression Number"),
                "number": value,
                "meaning": cls.destiny_number(number=num_value),
            }
        elif name == "active_number":
            interpretation = {
                "name": _("Active Number"),
                "number": value,
                "meaning": cls.active_number(number=num_value),
            }
        elif name == "birthdate_day_num":
            interpretation = {
                "name": _("Birthdate Day Number"),
                "number": value,
                "meaning": cls.birthdate_day_num(number=num_value),
            }
        elif name == "birthdate_month_num":
            interpretation = {
                "name": _("Birthdate Month Number"),
                "number": value,
                "meaning": cls.birthdate_month_num(number=num_value),
            }
        elif name == "birthdate_year_num":
            interpretation = {
                "name": _("Birthdate Year Number"),
                "number": value,
                "meaning": cls.birthdate_year_num(number=num_value),
            }
        elif name == "birthdate_year_num_alternative":
            interpretation = {
                "name": _("Birthdate Year Number Alternative"),
                "number": value,
                "meaning": cls.birthdate_year_num_alternative(number=num_value),
            }
        elif name == "attitude_number":
            interpretation = {
                "name": _("Attitude Number"),
                "number": value,
                "meaning": cls.attitude_number(number=num_value),
            }
        elif name == "power_number":
            interpretation = {
                "name": _("Power (Maturity) Number"),
                "number": value,
                "meaning": cls.power_number(number=num_value),
            }
        elif name == "power_number_alternative":
            interpretation = {
                "name": _("Power (Maturity) Number Alternative"),
                "number": value,
                "meaning": cls.power_number_alternative(number=num_value),
            }
        elif name == "karma_number":
            interpretation = {
                "name": _("Karma Number"),
                "number": value,
                "meaning": cls.karma_number(number=num_value),
            }
        elif name == "full_name_missing_numbers":
            # Ensure value is a tuple before passing to full_name_missing_numbers
            numbers_tuple = (value,) if isinstance(value, int) else tuple(value) if value is not None else ()
            interpretation = {
                "name": _("Karmic Lesson Numbers"),
                "number": value,
                "meaning": cls.full_name_missing_numbers(numbers=numbers_tuple),
            }
        elif name == "karmic_debt_numbers":
            # Ensure value is a dict[str, int]
            if isinstance(value, dict):
                numbers_dict = value
            elif isinstance(value, tuple):
                numbers_dict = {str(i): n for i, n in enumerate(value)}
            elif isinstance(value, int):
                numbers_dict = {"0": value}
            else:
                numbers_dict = {}
            interpretation = {
                "name": _("Karmic Debt Numbers"),
                "number": value,
                "meaning": cls.karmic_debt_numbers(numbers=numbers_dict),
            }
        return interpretation

    @classmethod
    def life_path_number(cls, number: int):
        return LifePathNumber.meanings.get(number, None)

    @classmethod
    def hearts_desire_number(cls, number: int):
        return HeartsDesireNumber.meanings.get(number, None)

    @classmethod
    def personality_number(cls, number: int):
        return PersonalityNumber.meanings.get(number, None)

    @classmethod
    def destiny_number(cls, number: int):
        return DestinyNumber.meanings.get(number, None)

    @classmethod
    def active_number(cls, number: int):
        return ActiveNumber.meanings.get(number, None)

    @classmethod
    def birthdate_day_num(cls, number: int):
        return DayNumber.meanings.get(number, None)

    @classmethod
    def birthdate_month_num(cls, number: int):
        return MonthNumber.meanings.get(number, None)

    @classmethod
    def birthdate_year_num(cls, number: int):
        return YearNumber.meanings.get(number, None)

    @classmethod
    def birthdate_year_num_alternative(cls, number: int):
        return YearNumber.meanings.get(number, None)

    @classmethod
    def attitude_number(cls, number: int):
        return AttitudeNumber.meanings.get(number, None)

    @classmethod
    def power_number(cls, number: int):
        return PowerNumber.meanings.get(number, None)

    @classmethod
    def power_number_alternative(cls, number: int):
        return PowerNumber.meanings.get(number, None)

    @classmethod
    def karma_number(cls, number: int):
        return KarmaNumber.meanings.get(number, None)

    @classmethod
    def full_name_missing_numbers(cls, numbers: tuple):
        if numbers is None:
            return None
        out_title = ""
        out_text = ""
        for n in numbers:
            meaning = KarmicLessonNumber.meanings.get(n, None)
            if meaning is not None:
                out_title += meaning["title"] + ", "
                out_text += meaning["description"] + " \n\n"
        return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @classmethod
    def karmic_debt_numbers(cls, numbers: Dict[str, int]):
        if numbers is None:
            return None
        out_title = ""
        out_text = ""
        for n in numbers.values():
            meaning = KarmicDebtNumber.meanings.get(n, None)
            if meaning is not None:
                out_title += meaning["title"] + ", "
                out_text += meaning["description"] + " \n\n"
        return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @property
    def meanings(self):
        return self._meanings
