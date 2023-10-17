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


class PersonalityNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Ambitious outlook"),
            "description": _(
                "You project a strong sense of individuality, leadership, and self-confidence. People see you as assertive and ambitious."
            ),
        },
        2: {
            "title": _("Cooperative outlook"),
            "description": _(
                "You come across as diplomatic, cooperative, and sensitive. Others perceive you as a peacemaker and mediator."
            ),
        },
        3: {
            "title": _("Enthusiastic outlook"),
            "description": _(
                "You have a vibrant and expressive personality. People see you as creative, sociable, and enthusiastic."
            ),
        },
        4: {
            "title": _("Practical outlook"),
            "description": _(
                "You appear to be practical, dependable, and hardworking. Others perceive you as stable and trustworthy."
            ),
        },
        5: {
            "title": _("Adventurous outlook"),
            "description": _(
                "You project a dynamic and adventurous persona. People see you as adaptable, free-spirited, and energetic."
            ),
        },
        6: {
            "title": _("Caring outlook"),
            "description": _(
                "You come across as nurturing, responsible, and caring. Others perceive you as a supportive and loving presence."
            ),
        },
        7: {
            "title": _("Intellectual outlook"),
            "description": _(
                "You have an aura of introspection and wisdom. People see you as intellectual, spiritual, and insightful."
            ),
        },
        8: {
            "title": _("Authoritative outlook"),
            "description": _(
                "You project an air of ambition and authority. Others perceive you as capable, powerful, and business-minded."
            ),
        },
        9: {
            "title": _("Compassionate outlook"),
            "description": _(
                "You appear to be compassionate, humanitarian, and idealistic. People see you as selfless and driven by a desire to help others."
            ),
        },
        11: {
            "title": _("Visionary outlook"),
            "description": _(
                "You project an aura of intuition and spiritual insight. Others perceive you as a visionary and inspirational leader."
            ),
        },
        22: {
            "title": _("Achiever outlook"),
            "description": _(
                "You come across as a master builder and manifestor of dreams. People see you as someone who can turn big ideas into reality."
            ),
        },
        33: {
            "title": _("Mentor outlook"),
            "description": _(
                "Your personality reflects a deep sense of compassion and a desire to uplift humanity. Others perceive you as a healer and mentor."
            ),
        },
    }
