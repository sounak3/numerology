import gettext
import locale
from typing import Dict
import os
import sys

localedir_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "..", "locale"
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
    language.install()
    _ = language.gettext
except:
    # If the current language does not have a translation, the default laguage (English) will be used English
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[default_lang]
    )
    language.install()
    _ = language.gettext


class YearNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Natural leaders, ambitious, and determined"),
            "description": _(
                "Individuals born in a year that reduces to 1 are often natural leaders, ambitious, and determined. They have a strong drive to succeed and excel in their endeavors."
            ),
        },
        2: {
            "title": _("Cooperative, sensitive, and diplomatic"),
            "description": _(
                "Those born in a year that reduces to 2 are typically cooperative, sensitive, and diplomatic. They are adept at creating harmony in their relationships and surroundings."
            ),
        },
        3: {
            "title": _("Creativity, communication skills, and self-expression"),
            "description": _(
                "People born in a year that reduces to 3 are known for their creativity, communication skills, and self-expression. They often have a vibrant and expressive personality."
            ),
        },
        4: {
            "title": _("Practical, hardworking, and stable"),
            "description": _(
                "Individuals born in a year that reduces to 4 are practical, hardworking, and stable. They have a strong sense of discipline and are committed to building a solid foundation in their lives."
            ),
        },
        5: {
            "title": _("Adventurous, dynamic, and freedom-loving"),
            "description": _(
                "Those born in a year that reduces to 5 are adventurous, dynamic, and freedom-loving. They seek change and variety, often enjoying new experiences and challenges."
            ),
        },
        6: {
            "title": _("Nurturing, responsible, and family-oriented"),
            "description": _(
                "People born in a year that reduces to 6 are nurturing, responsible, and family-oriented. They value harmony and often play a supportive role in their relationships and communities."
            ),
        },
        7: {
            "title": _("Introspective, spiritual, and analytical"),
            "description": _(
                "Individuals born in a year that reduces to 7 are often introspective, spiritual, and analytical. They possess a deep inner wisdom and have a strong desire for self-discovery."
            ),
        },
        8: {
            "title": _("Ambitious, authoritative, and success-driven"),
            "description": _(
                "Those born in a year that reduces to 8 are ambitious, authoritative, and success-driven. They have a strong desire for material success and often demonstrate leadership qualities."
            ),
        },
        9: {
            "title": _("Compassionate, idealistic, and humanitarian"),
            "description": _(
                "People born in a year that reduces to 9 are compassionate, idealistic, and humanitarian. They have a strong sense of empathy and are often dedicated to helping others and making a positive impact on the world."
            ),
        },
    }
