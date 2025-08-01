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
    # If the current language does not have a translation, the default language (English) will be used English
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[default_lang]
    )
    language.install()
    _ = language.gettext


class DayNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("I am important and independent"),
            "description": _(
                "You strongly believe in your individuality and independence. You think you are driven to achieve goals and a strong assertive personality."
            ),
        },
        2: {
            "title": _("I support and bring peace and balance"),
            "description": _(
                "You believe in your capability to understand others emotions. You think you can bring peace and harmony with your cooperation and diplomacy."
            ),
        },
        3: {
            "title": _("I am positive about myself and my goodness"),
            "description": _(
                "You believe there is a solution and you can make things alright. You see yourself as a creative, artistic, sociable, and enthusiastic personality."
            ),
        },
        4: {
            "title": _("I am practical, hard working and dependable"),
            "description": _(
                "You think you are practical and hardworking. You value stability and have methodical approach to life. Thats why you think you are stable and trustworthy."
            ),
        },
        5: {
            "title": _("I am dynamic free soul and free from bondages"),
            "description": _(
                "You think you are a dynamic and adventurous persona. You see yourself as adaptable, free-spirited, energetic and change loving personality."
            ),
        },
        6: {
            "title": _("I am a responsible and caring person"),
            "description": _(
                "You think you are a nurturing, caring, loving and responsible person. You prioritize family and community. And you think people love your supportive and loving presence."
            ),
        },
        7: {
            "title": _("I am a seeker, and have inner wisdom"),
            "description": _(
                "You think you have an aura of introspection and wisdom. You have a deep desire for inner growth and see yourself as intellectual, spiritual, and insightful personality."
            ),
        },
        8: {
            "title": _("I am powerful and can achieve anything"),
            "description": _(
                "You think you are capable, powerful, and business-minded. You seek financial security and think you can achieve that with your strong drive for material success and power."
            ),
        },
        9: {
            "title": _("I am compassionate and blessed by divine to help others"),
            "description": _(
                "You believe you're compassionate, humanitarian, and idealistic. You see yourself as selfless and driven by a desire to help whoever is in need."
            ),
        },
        11: {
            "title": _("I have a deep insight and an inspirational personality"),
            "description": _(
                "You think you have a spiritual insight and intuition. You see yourself as a visionary and an inspirational personality. You think your thoughts have a significant impact on others."
            ),
        },
        22: {
            "title": _("I am an achiever and build dreams to reality"),
            "description": _(
                "You believe in yourself as a master builder and realizer of dreams. You see yourself as someone who can overcome mammoth challenges and still turn big ambitions into reality."
            ),
        },
    }
