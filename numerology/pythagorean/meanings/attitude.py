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


class AttitudeNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("I project myself as independant and self made being"),
            "description": _(
                "You don't like to ask for help. You want to show a self-motivated, confident attitude that there's nothing that you can't achieve."
            ),
        },
        2: {
            "title": _("I show myself as a cooperative and understanding friend"),
            "description": _(
                "You want to be friendly. You want to show that you are sensitive to peoples feelings and always cooperate with them; and can mediate to bring peace."
            ),
        },
        3: {
            "title": _("I want to project my vibrance and make others vibe"),
            "description": _(
                "You don't want to be gloomy. You want to show your creativity, humor and positive vibrance by socializing with people and cheering up their mood with enthusiasm."
            ),
        },
        4: {
            "title": _("I want to show how practical and dependable I am"),
            "description": _(
                "You want to show your hardworking and dedicated nature. You want to show your practicality and trustworthiness by the level of detail you keep of everything happening."
            ),
        },
        5: {
            "title": _("I want to show my dynamic and adventurous persona"),
            "description": _(
                "You want to project a energetic and adventurous persona. To show people that you are life of the party, free-spirited and full of excitement. You adapt yourself accordingly."
            ),
        },
        6: {
            "title": _("I want to show I care and can fix broken hearts or businesses"),
            "description": _(
                "You want to project your nurturing, responsible, and caring nature. You want others to know you as a supportive being. That you can single-handedly fix relationships."
            ),
        },
        7: {
            "title": _("I want to present myself as a human of deep insight and wisdom"),
            "description": _(
                "You don't want people to guess your personal interests. However, overwhelm them with your deep understanding and wisdom of an ongoing topic. You want people to know you are as intellectual and spiritual."
            ),
        },
        8: {
            "title": _("I want to show myself as entrepreneur, owner and financially sound"),
            "description": _(
                "You project an air of ambition and authority. You want others to recognize your material success and achievements. You present your attitude as capable, powerful, and business-minded."
            ),
        },
        9: {
            "title": _("I want to present myself as compassionate and humanitarian"),
            "description": _(
                "You want to be idealistic. You project yourself as selfless and driven by a desire to help others. You never say no to someone seeking help and present yourself as compassionate and humanitarian."
            ),
        },
    }
