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


class ActiveNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Individuality"),
            "description": _(
                "Independence and leadership are associated with this number. You end up showing qualities of assertiveness and originality in daily life."
            ),
        },
        2: {
            "title": _("Balance"),
            "description": _(
                "Cooperation and diplomacy are prominent. In daily life you often end up balancing between opposing people and become peacemakers."
            ),
        },
        3: {
            "title": _("Jubilant"),
            "description": _(
                "Creativity and self-expression are highlighted. In daily life whatever way you chose, you end up becoming expressive and artistic."
            ),
        },
        4: {
            "title": _("Practical"),
            "description": _(
                "Stability and practicality are emphasized. Whatever cause you choose to work in daily life, you plan dedicatedly and work hard for it to complete."
            ),
        },
        5: {
            "title": _("Versatile"),
            "description": _(
                "Change and adaptability are key traits. You have a multi-focusing nature and end up diving in almost every opportunity or adventure in daily life."
            ),
        },
        6: {
            "title": _("Caring"),
            "description": _(
                "Nurturing and responsibility are prominent qualities. On daily life you often end up being caring and supportive."
            ),
        },
        7: {
            "title": _("Thoughtful"),
            "description": _(
                "Intellectual and introspective tendencies are associated with this number. In daily life you're often become thoughtful and insightful."
            ),
        },
        8: {
            "title": _("Goal oriented"),
            "description": _(
                "Ambition and material success are highlighted. In daily life you tend to be goal-oriented and business-minded."
            ),
        },
        9: {
            "title": _("Compassionate"),
            "description": _(
                "Compassion and humanitarianism are key traits. In daily life you often end up understanding and helping others."
            ),
        },
    }
