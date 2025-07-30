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


class KarmaNumber:

    meanings: Dict[int, Dict[str, str]] = {
        0: {
            "title": _("New beginning"),
            "description": _(
                "You might be a new soul, or maybe in your past life, you managed to fix many of your past mistakes. This life is like a new beginning for you, where you have the chance to start over with a fresh beginning and leave behind any previous burdens or troubles."
            ),
        },
        1: {
            "title": _("Karma result for ignoring self-worth"),
            "description": _(
                "The message from this karma number is about becoming self-reliant. It means that when you begin your life, you might rely on others a lot. However, the key lesson here is to learn to be independent and take care of yourself. This could show up as spending much of your life without a partner or being really successful but not relying on others much."
            ),
        },
        2: {
            "title": _("Karma result for ignoring righteousness"),
            "description": _(
                "The lesson to learn here is all about learning to cooperate with others. In your previous life, you might have used people, and now it's your turn to give back. You could end up with the job of looking after someone who relies on you. You'll also need to work on being less skeptical and trusting your gut feelings."
            ),
        },
        3: {
            "title": _("Karma result for ignoring responsibility"),
            "description": _(
                "In the past, you might have been careless, wasteful, and not always serious when you should have been. There's a chance you even took credit for someone else's work or used dishonest methods to succeed. In this life, your lesson is to be balanced, take things seriously, and be responsible."
            ),
        },
        4: {
            "title": _("Karma result for laziness and ignorance"),
            "description": _(
                "In your earlier life, you might have been lazy, so now you need to try your best. You might have to work harder than others to earn money. Your karma wants you to keep trying without giving up; you could become really successful if you keep doing the right things and don't give up easily."
            ),
        },
        5: {
            "title": _("Karma result for indiscipline"),
            "description": _(
                "In your previous life, you might have had issues with addiction, spending too much, or being too involved in romantic relationships. In this life, you'll have to work hard and give up some things to succeed later on. You might also face health problems that make you focus on staying healthy and doing the right things."
            ),
        },
        6: {
            "title": _("Karma result for ignoring relationships"),
            "description": _(
                "In your past life, you might have hurt or left your family. Now, you might have to take care of your family or someone who's sick. It might also be tough for you to move away from your family and be independent."
            ),
        },
        7: {
            "title": _("Karma result for ignorance of spirituality"),
            "description": _(
                "In the past, you might not have paid much attention to your spiritual side. You were really focused on making money. Now, it might be harder for you to earn money. You might also be dealing with an illness or long-term problem that makes you question your beliefs."
            ),
        },
        8: {
            "title": _("Karma result for misuse of authority"),
            "description": _(
                "In the past, you might have had a powerful position and used it in the wrong way. You might have also taken advantage of others for money. But in this life, you might not be in a powerful position. You might have less money than others and need to work really hard to succeed."
            ),
        },
        9: {
            "title": _("Karma result for ignoring empathy and kindness"),
            "description": _(
                "In your previous life, you might have avoided helping or caring for others. Now, your lesson is to be kind, caring, and assist people. You might start this life with your own problems, but you'll only do well once you learn to be a teacher or a generous person in your own way."
            ),
        },
    }
