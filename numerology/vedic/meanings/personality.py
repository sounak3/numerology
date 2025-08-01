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


class PersonalityNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Ambitious outlook"),
            "description": _(
                "People generally perceive number 1 individuals as authoritative, ambitious, and independent. They are likely to be respected and looked up to by those around them, especially in a professional setting. Their determined and strong-willed nature might lead others to view them as assertive and self-assured."
            ),
        },
        2: {
            "title": _("Cooperative outlook"),
            "description": _(
                "People generally perceive number 2 individuals as gentle, imaginative, and artistic. They might be seen as sensitive and inclined to moodiness if they are not surrounded by positive and happy environments. Their lack of self-confidence and tendency to be despondent if things are not going well might also be noticed."
            ),
        },
        3: {
            "title": _("Enthusiastic outlook"),
            "description": _(
                "People tend to perceive number 3 individuals as proud, independent, and authoritative. While they are not typically quarrelsome, their dictatorial nature and insistence on enforcing their ideas might lead them to make enemies. Their strong desire for independence and dislike for obligations might also be noticeable to others."
            ),
        },
        4: {
            "title": _("Rebellious outlook"),
            "description": _(
                "People perceive number 4 individuals as highly strung and sensitive. They are known to be devoted and loyal to their close circle of friends, often taking the side of the underdog in any argument or cause they support. Their tendency to challenge norms and take an opposing stance might lead them to have more secret enemies who work against them. They might be perceived as unconventional and unpredictable in their actions."
            ),
        },
        5: {
            "title": _("Energetic outlook"),
            "description": _(
                "People perceive number 5 individuals as highly energetic and quick-witted. They are often seen as risk-takers who are unafraid of challenges and are willing to take the necessary steps to achieve their goals. Their resilience and adaptability might be admired, although their tendency to exhaust their nervous energy and experience quick tempers under stress could be seen as a drawback."
            ),
        },
        6: {
            "title": _("Caring outlook"),
            "description": _(
                "People perceive number 6 individuals as warm, affectionate, and nurturing. They are often seen as devoted and selfless, willing to go to great lengths to support their loved ones. Their tendency to fight fiercely for what they believe in might be admired, but their aversion to discord and jealousy might be seen as a weakness."
            ),
        },
        7: {
            "title": _("Intellectual outlook"),
            "description": _(
                "People perceive number 7 individuals as independent thinkers with a strong sense of individuality. They are often admired for their unconventional approach to life and their inclination towards mystical and philosophical matters. Their magnetic and influential aura might draw people towards them, while their deep knowledge and wisdom might earn them respect in intellectual circles."
            ),
        },
        8: {
            "title": _("Authoritative outlook"),
            "description": _(
                "People perceive number 8 individuals as enigmatic figures, distinct from their peers and often misunderstood. Their actions and motives are often the subject of scrutiny and misinterpretation, leading to both praise and criticism. While some may recognize and appreciate their sacrifices and contributions, others might view them with suspicion or even condemnation."
            ),
        },
        9: {
            "title": _("Strong willed outlook"),
            "description": _(
                "They are often perceived as strong-willed and resilient personalities. While some may admire their courage and determination, others may view them as impulsive and quick-tempered. Their tendency to make enemies and engage in conflicts can lead to mixed opinions about their character. Despite the challenges they face, they are considered fortunate if they can control their fiery nature and avoid creating unnecessary conflicts."
            ),
        },
    }
