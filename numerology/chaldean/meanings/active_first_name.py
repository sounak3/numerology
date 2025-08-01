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
            "title": _("Leadership"),
            "description": _(
                "Number 1 individuals are likely to succeed in their endeavors. They resonate well with individuals born under the influence of the numbers 2, 4, and 7."
            ),
        },
        2: {
            "title": _("Harmony"),
            "description": _(
                "Number 2 individuals resonate well with individuals born under the influence of numbers 1 and 7, finding harmonious relationships with them."
            ),
        },
        3: {
            "title": _("Management"),
            "description": _(
                "Number 3 individuals are known to be successful in roles that require trust and responsibility due to their conscientious and commanding nature."
            ),
        },
        4: {
            "title": _("Stability"),
            "description": _(
                "Number 4 individuals might not achieve as much success in worldly or material matters as those born under other numbers."
            ),
        },
        5: {
            "title": _("Adaptability"),
            "description": _(
                "Number 5 individuals are known for their remarkable resilience and the ability to quickly recover from setbacks. They are often inclined towards speculative ventures and may find success in endeavors that require quick thinking and risk-taking."
            ),
        },
        6: {
            "title": _("Care"),
            "description": _(
                "Number 6 individuals are known for their ability to make a wide circle of friends, particularly with individuals born under the vibrations of 3, 6, and 9, or their respective series."
            ),
        },
        7: {
            "title": _("Wisdom"),
            "description": _(
                "Number 7 individuals are likely to be successful in fields that involve exploration, travel, or intellectual pursuits. They might excel in writing, painting, or poetry, incorporating their philosophical perspectives into their creative works."
            ),
        },
        8: {
            "title": _("Achievement"),
            "description": _(
                "Number 8 individuals tend to experience extreme highs and lows in their lives. They may achieve great success or face significant failures, with little middle ground."
            ),
        },
        9: {
            "title": _("Resilience"),
            "description": _(
                "Individuals influenced by the number 9 often experience conflict and strife, both in their personal relationships and in their endeavors. Despite the challenges they face, they display a strong determination and a willingness to overcome obstacles, ultimately achieving success through their relentless efforts."
            ),
        },
    }
