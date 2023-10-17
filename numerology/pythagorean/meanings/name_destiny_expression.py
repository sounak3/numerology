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


class DestinyNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Born to lead"),
            "description": _(
                "You have the potential for leadership, independence, and individuality. Your destiny will involve self-discovery, creating new opportunity and pioneering in them. You may do this with your potentials mentioned above or with your Life path forces."
            ),
        },
        2: {
            "title": _("Born to bring equilibrium"),
            "description": _(
                "Your destiny is tied to cooperation, diplomacy, and building partnerships. Your destiny will involve bringing balance and harmony. You may do this with help of your charm, understanding and ability to persue, or with your Life path forces."
            ),
        },
        3: {
            "title": _("Born to create"),
            "description": _(
                "Your destiny involves self-expression, creativity, and communication. Your destiny will make you a saviour, a symbol of hope, a resolver of difficult most problems of life. You may do this with your God gifted talents of creativity, joy and communication, Or with your Life path forces."
            ),
        },
        4: {
            "title": _("Born to stabilize"),
            "description": _(
                "You are meant for responsibility, stability, order, and practicality. Your destiny will involve building a solid foundation for self or family or clan or your loved ones, and achieving a sense of security for them. Your Life path forces may help you achieve these goals."
            ),
        },
        5: {
            "title": _("Born to change"),
            "description": _(
                "Your life's purpose is to embrace change, adaptability, and freedom. Your destiny will lead you to bring a change, bring a new order or transform an old one. You are here to bring revolution in some sphere with your dynamism and adventurous nature Or with your Life path potentials."
            ),
        },
        6: {
            "title": _("Born for caring"),
            "description": _(
                "You are destined to provide care, support, and love to others. To fall and rise emotionally and create benchmarks in trust and emotional intelligence. Your family, community, service-oriented endeavors Or your life path energies may help you to do so."
            ),
        },
        7: {
            "title": _("Born to have inner wisdom"),
            "description": _(
                "Your destiny involves seeking inner wisdom, introspection, and spiritual understanding. You will be drawn to spiritual or intellectual pursuits, providing answers to self and humanity about deeper questions of life. Your life path forces may aid in the same."
            ),
        },
        8: {
            "title": _("Born to achieve"),
            "description": _(
                "Your path is connected to material success, ambition, and power. You are meant to make a significant impact in the material world, making yourself, family, loved ones or clan materialistically future ready. Your life path forces may aid in the same."
            ),
        },
        9: {
            "title": _("Born for compassion"),
            "description": _(
                "Your life's purpose is to serve humanity and promote compassion. You will be drawn to humanitarian or charitable efforts. Blessed by the divine, your destiny will lead you to understand and help the needy. Your life path forces may aid in the same."
            ),
        },
        11: {
            "title": _("Born to inspire"),
            "description": _(
                "You have a spiritual and inspirational destiny. Your path involves intuition and enlightenment. Guiding others toward higher consciousness through teaching, presenting and public speaking, etc. Your life path forces may aid in the same."
            ),
        },
        22: {
            "title": _("Born to realize good dreams"),
            "description": _(
                "Your destiny is to be a master builder and visionary. Instability, struggles and adverse situations Or your life path forces in earlier phase of life, may make you self-reliant and strong. You have the potential to turn big dreams into tangible reality on a large scale."
            ),
        },
        33: {
            "title": _("Born to guide and realize"),
            "description": _(
                "Your destiny is deeply rooted in compassion and healing. Gifted with high-energy, outstanding creative and artistic abilities, you are meant to uplift humanity and serve as a spiritual guide (also if your life path aids in the same). To make the world better and more beautiful."
            ),
        },
    }
