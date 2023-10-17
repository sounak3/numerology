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


class KarmicLessonNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Learning self-worth"),
            "description": _(
                "If your karmic lesson number is 1, you need to learn to be more independent and take charge. You might find it hard to speak up for yourself and take the first step, but you'll need to learn how to be assertive and in control."
            ),
        },
        2: {
            "title": _("Learning cooperation"),
            "description": _(
                "For a karmic lesson number of 2, your lesson is about being patient, cooperative and diplomatic. You might struggle with finding balance in relationships, but it's important to learn how to compromise and work well with others."
            ),
        },
        3: {
            "title": _("Learning to express yourself"),
            "description": _(
                "With a karmic lesson number 3, you should focus on expressing yourself creatively and speaking up clearly. If you find it hard to share your feelings or ideas, practice communicating confidently and openly."
            ),
        },
        4: {
            "title": _("Learning discipline with flexibility"),
            "description": _(
                "If your karmic lesson number is 4, you need to work on being more flexible and adaptable while being organized and disciplined. Being too strict and inflexible can be a problem, so try to embrace change and keep an open mind."
            ),
        },
        5: {
            "title": _("Learning to be adventurous"),
            "description": _(
                "For a karmic lesson number of 5, your goal is to embrace change and take risks. Feeling stuck or bored can be a challenge, but trying new things with curiosity and being adventurous will help you grow."
            ),
        },
        6: {
            "title": _("Learning relationships and loving yourself"),
            "description": _(
                "If your karmic lesson number is 6, learn to take care of yourself while also caring for others. Being too selfless might be difficult, so set boundaries and make sure your needs are met too."
            ),
        },
        7: {
            "title": _("Learn to develop your spiritual side"),
            "description": _(
                "For a karmic lesson number of 7, trust your instincts and connect with your spiritual side. If you tend to overthink and doubt yourself, practice listening to your inner voice and believing in your intuition."
            ),
        },
        8: {
            "title": _("Learn to be self-disciplined"),
            "description": _(
                "With a karmic lesson number of 8, find a balance between ambition and spiritual growth. Avoid being overly focused on material success and learn to prioritize your spiritual well-being as well."
            ),
        },
        9: {
            "title": _("Learn to help and understand"),
            "description": _(
                "If your karmic lesson number is 9, work on finding a balance between helping others and taking care of yourself. Being too selfless can be challenging, so make sure to also pay attention to your own needs."
            ),
        },
    }
