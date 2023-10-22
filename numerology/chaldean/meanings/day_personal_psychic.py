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
    # If the current language does not have a translation, the default language (English) will be used English
    language = gettext.translation(
        "numerology", localedir=localedir_path, languages=[default_lang]
    )
    language.install()
    _ = language.gettext


class DayNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("I am ambitious and determined"),
            "description": _(
                "You believe you've an ambitious and determined outlook. That your authoritative and independent nature often earns you respect and admiration in various professional settings. You believe your drive and determination are key to your success."
            ),
        },
        2: {
            "title": _("I am Cooperative and bring harmony"),
            "description": _(
                "You perceive yourself as gentle and imaginative, with a touch of sensitivity. You think you strive to maintain a cooperative and harmonious environment, although sometimes facing moments of self-doubt and despondency when things don't go as planned. You believe your ability to foster positive relationships is essential to your well-being."
            ),
        },
        3: {
            "title": _("I am proud and independent spirit"),
            "description": _(
                "You believe in your independent spirit, coupled with a strong sense of authority. While you try to avoid conflicts, you think people don't like your ideas and beliefs. You value your independence greatly and strive to create a life that aligns with your vision."
            ),
        },
        4: {
            "title": _("I am protector of the powerless"),
            "description": _(
                "You consider yourself highly devoted and loyal to your inner circle, often standing up for those in need. You think your inclination to challenge norms generally does not always sit well with everyone. While some may perceive you as unpredictable, you believe your unwavering support for the underdog remains a defining aspect of your character."
            ),
        },
        5: {
            "title": _("I am witty and productive as well"),
            "description": _(
                "You see myself as highly energetic and quick-witted, unafraid of taking risks and embracing challenges. You believe your adaptability and resilience are key attributes, although you acknowledge the need to manage your nervous energy and temper during stressful situations. You believe in your enthusiastic and productive endeavors."
            ),
        },
        6: {
            "title": _("I am a caring and supportive individual"),
            "description": _(
                "You identify yourself with a warm and nurturing nature, dedicated to support and care your loved ones. You think you're a defender of your strong convictions, however, strive to maintain harmony and avoid discord. You believe your commitment to create a positive and loving environment is unwavering."
            ),
        },
        7: {
            "title": _("I am an independent wisdom seeker"),
            "description": _(
                "You recognize your independent thinking and strong individuality, often drawn towards mystical and philosophical matters. You think your magnetic and influential presence sometimes attract others, and your deep knowledge and wisdom contribute to your respected position in intellectual circles. You value your unconventional approach to life and continuously seek personal growth through intellectual pursuits."
            ),
        },
        8: {
            "title": _("I am a misunderstood builder"),
            "description": _(
                "You think you are often misunderstood and subject to both praise and criticism. You believe your actions and motives are to build and guide people, but are often open to misinterpretation, leading to a range of opinions about your character. While you appreciate recognition for your sacrifices and contributions, you're aware that your individuality may sometimes evoke suspicion or even condemnation."
            ),
        },
        9: {
            "title": _("I am a soldier of life"),
            "description": _(
                "You see yourself as a strong willed and resilient persona, willing to face challenges head-on. You know that some appreciate your courage and determination, while others think you as impulsive and quick-tempered. You acknowledge the need to manage conflicts and control your fiery nature to avoid unnecessary discord. You believe your strength lies in your ability to persevere through adversity and maintain a determined spirit."
            ),
        },
    }
