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
    # If the current language does not have a translation, the default laguage (English) will be used English
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
    def get_interpretation(cls, name: str, value: int):
        interpretation = None
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
        elif name == "birthdate_day_num":
            interpretation = {
                "name": _("Birthdate Day Number"),
                "number": value,
                "meaning": cls.birthdate_day_num(number=value),
            }
        elif name == "birthdate_year_num_alternative":
            interpretation = {
                "name": _("Age Number"),
                "number": value,
                "meaning": "The year when you are aged " + str(value) + " will be an important year of your life.",
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

    @property
    def meanings(self):
        return self._meanings
