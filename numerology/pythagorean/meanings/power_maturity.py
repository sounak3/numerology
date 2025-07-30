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


class PowerNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Become more self-reliant with growing age"),
            "description": _(
                "Individuals with a Power or Maturity Number of 1 are likely to develop increased self-confidence, independence, and leadership skills as they mature. They may become more assertive and driven to achieve their goals."
            ),
        },
        2: {
            "title": _("With age become collaborative and peace making"),
            "description": _(
                "Those with a Power or Maturity Number of 2 may experience a deepening sense of cooperation, diplomacy, and emotional sensitivity. They may become more adept at fostering harmony in their relationships."
            ),
        },
        3: {
            "title": _("With age become more joyful and expressive"),
            "description": _(
                "Individuals with a Power or Maturity Number of 3 may further develop their creativity, self-expression, and communication skills. They may find more opportunities for artistic expression and creative pursuits."
            ),
        },
        4: {
            "title": _("As they mature they become workoholic and perfectionist"),
            "description": _(
                "Those with a Power or Maturity Number of 4 may focus on cultivating stability, practicality, and a strong work ethic. They may become more skilled at building a solid foundation for themselves and others."
            ),
        },
        5: {
            "title": _("As they mature they embrace change easily and love dynamism"),
            "description": _(
                "Individuals with a Power or Maturity Number of 5 may embrace change, adventure, and freedom as they mature. They may seek new experiences and pursue personal growth and development."
            ),
        },
        6: {
            "title": _("With age they become caring and responsible"),
            "description": _(
                "Those with a Power or Maturity Number of 6 may deepen their sense of responsibility, nurturing, and compassion. They may prioritize their roles as caregivers and focus on creating harmony within their families and communities."
            ),
        },
        7: {
            "title": _("With maturity their wisdom and spirituality increases"),
            "description": _(
                "Individuals with a Power or Maturity Number of 7 may further explore their introspective and spiritual side. They may seek deeper wisdom, understanding, and personal growth through introspection and self-discovery."
            ),
        },
        8: {
            "title": _("They become ambitious and materialistic with age"),
            "description": _(
                "Those with a Power or Maturity Number of 8 may focus on material success, ambition, and achieving their goals. They may develop strong leadership skills and a drive for financial security and abundance."
            ),
        },
        9: {
            "title": _("They become compassionate and selfless as they grow older"),
            "description": _(
                "Individuals with a Power or Maturity Number of 9 may deepen their sense of compassion, philanthropy, and humanitarianism. They may become more dedicated to making a positive impact on the world and helping those in need."
            ),
        },
    }
