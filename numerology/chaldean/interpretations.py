import gettext
import locale
import os
import sys
from typing import Dict, List, Optional

import numerology.pythagorean.interpretations as pInterpretations
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
    raise
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


class Interpretations(pInterpretations.Interpretations):

    key_figures: Dict = {}
    _meanings: Dict = {}

    def __init__(self, key_figures: Dict):
        self.key_figures = key_figures
        self.get_all_interpretations()

    def get_all_interpretations(self):
        for k, v in self.key_figures.items():
            self._meanings[k] = self.get_interpretation(k, v)

    @classmethod
    def get_num_from_value(cls, value) -> int:
        if isinstance(value, str) and value.isdigit():
            return int(value)
        elif isinstance(value, str):
            return 0
        elif isinstance(value, int):
            return value
        elif isinstance(value, (list, tuple)):
            return int(''.join(map(str, value)) or 0)
        else:
            return 0

    @classmethod
    def get_interpretation(cls, name: str, value: tuple):
        num_value = cls.get_num_from_value(value)

        if isinstance(value, tuple) and len(value) > 1:
            interpretation = super().get_interpretation(name, value[1])
        elif isinstance(value, tuple) and len(value) == 1:
            interpretation = super().get_interpretation(name, value[0])
        else:
            interpretation = super().get_interpretation(name, value)

        if name == "life_path_number":
            interpretation = {
                "name": _("Life Path Number"),
                "number": value,
                "meaning": cls.life_path_number(number=num_value),
            }
        elif name == "name_number":
            interpretation = {
                "name": _("Name Number"),
                "number": value,
                "meaning": cls.name_number(number=value),
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
        elif name == "birthdate_year_num_alternative":
            interpretation = {
                "name": _("Age Number"),
                "number": value,
                "meaning": "The year when you are aged " + str(value) + " will be an important year of your life.",
            }
        return interpretation

    @classmethod
    def life_path_number(cls, number: int):
        if number is None:
            return None
        elif isinstance(number, int):
            return LifePathNumber.meanings.get(number, None)
        else:
            out_title = ""
            out_text = ""
            comp_text = ""
            for n in number:
                if n < 10:
                    meaning = LifePathNumber.meanings.get(n, None)
                    if meaning is not None:
                        out_title += meaning["title"] + ", "
                        out_text += meaning["description"] + " \n\n"
                else:
                    comp_meaning = CompoundNumber.meanings.get(n, None)
                    if comp_meaning is not None:
                        comp_text += comp_meaning["title"] + ": "
                        comp_text += comp_meaning["description"] + " \n\n"
            out_text += comp_text
            return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @classmethod
    def birthdate_day_num(cls, number: int):
        if number is None:
            return None
        elif isinstance(number, int):
            return super().birthdate_day_num(number)
        else:
            out_title = ""
            out_text = ""
            comp_text = ""
            for n in number:
                if n < 10:
                    meaning = DayNumber.meanings.get(n, None)
                    if meaning is not None:
                        out_title += meaning["title"] + ", "
                        out_text += meaning["description"] + " \n\n"
                else:
                    comp_meaning = CompoundNumber.meanings.get(n, None)
                    if comp_meaning is not None:
                        comp_text += comp_meaning["title"] + ": "
                        comp_text += comp_meaning["description"] + " \n\n"
            out_text += comp_text
            return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @classmethod
    def name_number(cls, number: tuple):
        if number is None:
            return None
        elif isinstance(number, int):
            return DestinyNumber.meanings.get(number, None)
        else:
            out_title = ""
            out_text = ""
            comp_text = ""
            for n in number:
                if n < 10:
                    meaning = DestinyNumber.meanings.get(n, None)
                    if meaning is not None:
                        out_title += meaning["title"] + ", "
                        out_text += meaning["description"] + " \n\n"
                else:
                    comp_meaning = CompoundNumber.meanings.get(n, None)
                    if comp_meaning is not None:
                        comp_text += comp_meaning["title"] + ": "
                        comp_text += comp_meaning["description"] + " \n\n"
            out_text += comp_text
            return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @classmethod
    def active_number(cls, number: int):
        if number is None:
            return None
        elif isinstance(number, int):
            return super().active_number(number)
        else:
            out_title = ""
            out_text = ""
            comp_text = ""
            for n in number:
                if n < 10:
                    meaning = ActiveNumber.meanings.get(n, None)
                    if meaning is not None:
                        out_title += meaning["title"] + ", "
                        out_text += meaning["description"] + " \n\n"
                else:
                    comp_meaning = CompoundNumber.meanings.get(n, None)
                    if comp_meaning is not None:
                        comp_text += comp_meaning["title"] + ": "
                        comp_text += comp_meaning["description"] + " \n\n"
            out_text += comp_text
            return {"title": out_title.rstrip(", "), "description": out_text.rstrip("\n")}

    @property
    def meanings(self):
        return self._meanings
