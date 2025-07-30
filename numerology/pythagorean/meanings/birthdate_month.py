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
except Exception:
    # If unable to get the locale language, use English
    lang = default_lang
try:
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[lang]
    )
    language.install()
    _ = language.gettext
except Exception:
    # If the current language does not have a translation, the default laguage (English) will be used English
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[default_lang]
    )
    language.install()
    _ = language.gettext


class MonthNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("January born"),
            "description": _(
                "People born in January tend to be independent, self-reliant, and natural leaders. They often have a strong sense of individuality and a desire for achievement."
            ),
        },
        2: {
            "title": _("February born"),
            "description": _(
                "Those born in February are often cooperative, diplomatic, and peace-loving. They value harmony and are skilled at building relationships."
            ),
        },
        3: {
            "title": _("March born"),
            "description": _(
                "People born in March are typically creative, expressive, and outgoing. They have a natural talent for communication and self-expression."
            ),
        },
        4: {
            "title": _("April born"),
            "description": _(
                "Those born in April are known for their practicality, stability, and hard work. They excel in structured and organized environments."
            ),
        },
        5: {
            "title": _("May born"),
            "description": _(
                "May-born individuals are adventurous, dynamic, and free-spirited. They have a desire for change and enjoy exploring new experiences."
            ),
        },
        6: {
            "title": _("June born"),
            "description": _(
                "People born in June are often nurturing, responsible, and family-oriented. They have a strong sense of duty and care for their loved ones."
            ),
        },
        7: {
            "title": _("July born"),
            "description": _(
                "Those born in July tend to be introspective, intuitive, and spiritually inclined. They have a deep interest in inner growth and self-discovery."
            ),
        },
        8: {
            "title": _("August born"),
            "description": _(
                "August-born individuals are ambitious, determined, and focused on material success. They are often driven to achieve financial security."
            ),
        },
        9: {
            "title": _("September born"),
            "description": _(
                "People born in September are compassionate, humanitarian, and idealistic. They have a strong desire to help others and make a positive impact."
            ),
        },
        10: {
            "title": _("October born"),
            "description": _(
                "October-born individuals combine the qualities of 1 and 0 (which represents potential). They are often seen as innovative leaders with the potential for achievement."
            ),
        },
        11: {
            "title": _("November born"),
            "description": _(
                "November-born individuals often possess spiritual insight and intuition. They are seen as inspirational and may have a significant impact on others."
            ),
        },
        12: {
            "title": _("December born"),
            "description": _(
                "December-born individuals combine the qualities of 1 and 2. They are cooperative and diplomatic leaders who value harmony in their pursuits."
            ),
        },
    }
