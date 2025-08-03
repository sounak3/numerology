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


class LegacyNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("The Pioneer's Legacy"),
            "description": _(
                "You inherit a legacy of trailblazing and breaking new ground. You may come from a line of people who stood apart or had to be self-reliant. Your influence lies in inspiring others to be bold, original, and self-starting."
            ),
        },
        2: {
            "title": _("The Peacemaker's Legacy"),
            "description": _(
                "You carry a legacy of support, healing, and relationship-building. Your family line may have been defined by behind-the-scenes strength, service, or emotional intelligence."
            ),
        },
        3: {
            "title": _("The Artist's Legacy"),
            "description": _(
                "You come from a lineage where expression, storytelling, or charisma may have been prominent (or suppressed). Your gift is uplifting others with your voice, humor, or creative vision."
            ),
        },
        4: {
            "title": _("The Builder's Legacy"),
            "description": _(
                "Your legacy is about hard work, tradition, and foundations. Your family may have valued duty, order, or practicality. You build things — businesses, systems, or families — that last through generations."
            ),
        },
        5: {
            "title": _("The Freedom-Seeker's Legacy"),
            "description": _(
                "You inherit a legacy of movement, rebellion, or breaking away from limitations. Your lineage may have faced constraints — and now you're here to bring freedom, innovation, and adaptability."
            ),
        },
        6: {
            "title": _("The Nurturer's Legacy"),
            "description": _(
                "You carry a legacy of caregiving and sacrifice. Perhaps your ancestors were caretakers, teachers, or protectors. Your impact lies in how deeply you love, heal, and serve your community or family."
            ),
        },
        7: {
            "title": _("The Seeker's Legacy"),
            "description": _(
                "Your lineage may include mystics, thinkers, or those misunderstood for their inner depth. You're here to carry forward a legacy of intellectual and spiritual refinement."
            ),
        },
        8: {
            "title": _("The Power-Holder's Legacy"),
            "description": _(
                "You come from a line where power, control, or wealth played a role — whether positively or through struggle. You're here to master influence and integrity, leaving a mark of leadership and abundance."
            ),
        },
        9: {
            "title": _("The Humanitarian's Legacy"),
            "description": _(
                "Your legacy is one of universal love, compassion, and giving back. You may feel called to heal collective wounds, inspired by ancestral struggles or service. You are the 'closer' of karmic cycles."
            ),
        },
        11: {
            "title": _("The Spiritual Illuminator's Legacy"),
            "description": _(
                "You come from a lineage marked by spiritual gifts or emotional intensity. Your legacy is to be a light for others, raising consciousness through words, vision, or healing."
            ),
        },
        22: {
            "title": _("The Master Builder's Legacy"),
            "description": _(
                "You have the ability to bring big visions into the physical world. Your legacy is practical magic - turning dreams into lasting realities for others. You may finish what others before you couldn't."
            ),
        },
        33: {
            "title": _("The Master Healer's Legacy"),
            "description": _(
                "You carry a deep legacy of selfless service, healing, and transformation. Often, there's ancestral pain or sacrifice you're here to heal. You embody divine love and service in its purest form."
            ),
        },
    }
