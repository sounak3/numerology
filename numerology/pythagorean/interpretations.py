import gettext
import locale
import os
import sys
from typing import Dict, List, Optional

from .meanings import LifePathNumber, HeartsDesireNumber, PersonalityNumber, DestinyNumber, ActiveNumber, DayNumber, MonthNumber, YearNumber, AttitudeNumber, PowerNumber, KarmaNumber, KarmicLessonNumber, KarmicDebtNumber, LegacyNumber

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
    def get_num_from_value(cls, value) -> int | None:
        if isinstance(value, str) and value.isdigit():
            return int(value)
        elif isinstance(value, str):
            raise ValueError("Invalid value: "+ value +". Expected a number or a tuple of numbers or a string representing a number.")
        elif isinstance(value, int):
            return value
        elif isinstance(value, (list, tuple)):
            return int(''.join(map(str, value)) or 0)
        else:
            return 0
        
    @classmethod
    def get_dict_from_value(cls, value) -> Dict[str, int]:
        if isinstance(value, dict):
            return value
        elif isinstance(value, tuple):
            return {str(i): n for i, n in enumerate(value)}
        elif isinstance(value, int):
            return {"0": value}
        else:
            return {}
    
    @classmethod
    def get_tuple_from_value(cls, value) -> tuple:
        if isinstance(value, tuple):
            return value
        elif isinstance(value, int):
            return (value,)
        elif isinstance(value, str) and value.isdigit():
            return (int(value),)
        elif value is not None:
            return tuple(value)
        else:
            return ()

    @classmethod
    def get_interpretation(cls, name: str, value):
        interpretation = None

        if name in {"first_name", "last_name", "birthdate"}:
            interpretation = value
        elif name == "life_path_number":
            interpretation = {
                "name": _("Life Path Number"),
                "number": value,
                "meaning": cls.life_path_number(number=value),
            }
        elif name == "life_path_number_alternative":
            interpretation = {
                "name": _("Life Path Number Alternative"),
                "number": value,
                "meaning": cls.life_path_number(number=value),
            }
        elif name == "hearts_desire_number":
            interpretation = {
                "name": _("Hearts Desire (Soul urge) Number"),
                "number": value,
                "meaning": cls.hearts_desire_number(number=value),
            }
        elif name == "personality_number":
            interpretation = {
                "name": _("Personality Number"),
                "number": value,
                "meaning": cls.personality_number(number=value),
            }
        elif name == "destiny_number":
            interpretation = {
                "name": _("Destiny Number"),
                "number": value,
                "meaning": cls.destiny_number(number=value),
            }
        elif name == "expression_number":
            interpretation = {
                "name": _("Expression Number"),
                "number": value,
                "meaning": cls.destiny_number(number=value),
            }
        elif name == "active_number":
            interpretation = {
                "name": _("Active Number"),
                "number": value,
                "meaning": cls.active_number(number=value),
            }
        elif name == "legacy_number":
            interpretation = {
                "name": _("Legacy Number"),
                "number": value,
                "meaning": cls.legacy_number(number=value),
            }
        elif name == "birthdate_day_num":
            interpretation = {
                "name": _("Birthdate Day Number"),
                "number": value,
                "meaning": cls.birthdate_day_num(number=value),
            }
        elif name == "birthdate_month_num":
            interpretation = {
                "name": _("Birthdate Month Number"),
                "number": value,
                "meaning": cls.birthdate_month_num(number=value),
            }
        elif name == "birthdate_year_num":
            interpretation = {
                "name": _("Birthdate Year Number"),
                "number": value,
                "meaning": cls.birthdate_year_num(number=value),
            }
        elif name == "birthdate_year_num_alternative":
            interpretation = {
                "name": _("Birthdate Year Number Alternative"),
                "number": value,
                "meaning": cls.birthdate_year_num_alternative(number=value),
            }
        elif name == "attitude_number":
            interpretation = {
                "name": _("Attitude Number"),
                "number": value,
                "meaning": cls.attitude_number(number=value),
            }
        elif name == "power_number":
            interpretation = {
                "name": _("Power (Maturity) Number"),
                "number": value,
                "meaning": cls.power_number(number=value),
            }
        elif name == "power_number_alternative":
            interpretation = {
                "name": _("Power (Maturity) Number Alternative"),
                "number": value,
                "meaning": cls.power_number_alternative(number=value),
            }
        elif name == "karma_number":
            interpretation = {
                "name": _("Karma Number"),
                "number": value,
                "meaning": cls.karma_number(number=value),
            }
        elif name == "full_name_missing_numbers":
            numbers_tuple = cls.get_tuple_from_value(value)
            interpretation = {
                "name": _("Karmic Lesson Numbers"),
                "number": value,
                "meaning": cls.full_name_missing_numbers(numbers=numbers_tuple),
            }
        elif name == "karmic_debt_numbers":
            numbers_dict = cls.get_dict_from_value(value)
            interpretation = {
                "name": _("Karmic Debt Numbers"),
                "number": tuple(value.values()) if isinstance(value, dict) else value,
                "meaning": cls.karmic_debt_numbers(numbers=numbers_dict),
            }
        elif name == "full_name_numbers":
            numbers_dict = cls.get_dict_from_value(value)
            interpretation = {
                "name": _("Full Name Numbers"),
                "number": tuple(value.keys()) if isinstance(value, dict) else value,
                "meaning": cls.full_name_numbers(numbers=numbers_dict),
            }
        return interpretation

    @classmethod
    def life_path_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return LifePathNumber.meanings.get(num_value, None)

    @classmethod
    def hearts_desire_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return HeartsDesireNumber.meanings.get(num_value, None)

    @classmethod
    def personality_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return PersonalityNumber.meanings.get(num_value, None)

    @classmethod
    def destiny_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return DestinyNumber.meanings.get(num_value, None)

    @classmethod
    def active_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return ActiveNumber.meanings.get(num_value, None)

    @classmethod
    def birthdate_day_num(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return DayNumber.meanings.get(num_value, None)

    @classmethod
    def birthdate_month_num(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return MonthNumber.meanings.get(num_value, None)

    @classmethod
    def birthdate_year_num(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return YearNumber.meanings.get(num_value, None)

    @classmethod
    def birthdate_year_num_alternative(cls, number: int | None):
        return cls.birthdate_year_num(number)

    @classmethod
    def attitude_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return AttitudeNumber.meanings.get(num_value, None)

    @classmethod
    def power_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return PowerNumber.meanings.get(num_value, None)

    @classmethod
    def power_number_alternative(cls, number: int | None):
        return cls.power_number(number)

    @classmethod
    def karma_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return KarmaNumber.meanings.get(num_value, None)

    @classmethod
    def full_name_numbers(cls, numbers: Dict[str, int]):
        if numbers is None:
            return None
        out_title = "Details, "
        out_text = ""
        for n in numbers.keys():
            out_text += str(n) + " - " + str(numbers[n]) + " times. \n"
        return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @classmethod
    def legacy_number(cls, number: int | None):
        num_value = cls.get_num_from_value(number)
        if num_value is None:
            return None
        return LegacyNumber.meanings.get(num_value, None)

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
        out_title = "Details, "
        out_text = ""
        for n in numbers.keys():
            meaning = KarmicDebtNumber.meanings.get(numbers[n], None)
            if meaning is not None:
                out_text += n + " - " + str(numbers[n]) + " - \n" + meaning["description"] + " \n\n"
        return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @property
    def meanings(self):
        return self._meanings
