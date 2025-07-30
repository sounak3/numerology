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


class HeartsDesireNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Desire of self-achievement"),
            "description": _(
                "Independence and self-achievement are important to you. You desire personal success and recognition."
            ),
        },
        2: {
            "title": _("Desire of collaboration"),
            "description": _(
                "You crave harmony, cooperation, and loving relationships. Your heart's desire is to be in a partnership or to nurture others."
            ),
        },
        3: {
            "title": _("Desire for self-expression"),
            "description": _(
                "Creativity, self-expression, and joy are your deepest desires. You seek outlets for your artistic and communicative talents."
            ),
        },
        4: {
            "title": _("Desire of perfection"),
            "description": _(
                "You value stability, order, and structure. Your heart's desire is to build a solid foundation in your life."
            ),
        },
        5: {
            "title": _("Desire of change"),
            "description": _(
                "Freedom and adventure are what you desire most. You yearn for variety, change, and the excitement of new experiences."
            ),
        },
        6: {
            "title": _("Desire for emotional harmony"),
            "description": _(
                "Your heart's desire is to create a harmonious and loving home. You want to care for and support your loved ones."
            ),
        },
        7: {
            "title": _("Desire of inner wisdom"),
            "description": _(
                "You seek inner wisdom, spiritual understanding, and introspection. Your heart's desire is to explore the mysteries of life."
            ),
        },
        8: {
            "title": _("Desire of material success"),
            "description": _(
                "Material success, achievement, and power are your desires. You want to make a significant impact in the material world."
            ),
        },
        9: {
            "title": _("Desire of ideal world"),
            "description": _(
                "Your heart's desire is to help others and make the world a better place. You're motivated by compassion and humanitarianism."
            ),
        },
        11: {
            "title": _("Desire for deeper understanding"),
            "description": _(
                "You have a deep desire for spiritual enlightenment and intuition. You aspire to inspire others through your insights."
            ),
        },
        22: {
            "title": _("Desire of significant achievement"),
            "description": _(
                "Your heart's desire is to manifest your grandest visions into reality. You're a master builder and dreamer."
            ),
        },
        33: {
            "title": _("Desire to heal the world"),
            "description": _(
                "You desire to uplift humanity and bring healing to the world. You have a profound sense of responsibility and love for others."
            ),
        },
    }
