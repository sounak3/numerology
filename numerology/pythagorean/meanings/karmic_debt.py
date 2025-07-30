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


class KarmicDebtNumber:

    meanings: Dict[int, Dict[str, str]] = {
        13: {
            "title": _("Abuse of ethics, morals and communication"),
            "description": _(
                "The karmic debt number 13 reflects a pattern of struggles in completing tasks and may indicate a history of misuse of words or abusing morals for personal gain. Individuals with this karmic debt often face obstacles and frustrations in achieving their goals, leading to feelings of futility and the temptation to give up. However, success is attainable through perseverance and a focused, organized approach, avoiding shortcuts and taking responsibility for one's actions. Those with this karmic debt should strive to maintain concentration, avoid procrastination, and stay disciplined in their endeavors, learning to manage challenges without succumbing to negativity or laziness."
            ),
        },
        14: {
            "title": _("Abuse of time, freedom and temptation"),
            "description": _(
                "The karmic debt number 14 signifies a history of misusing freedom, leading to a pattern of experiencing constant changes and unexpected circumstances. Individuals with this karmic debt may struggle with self-discipline, overindulgence, and addictive behaviors related to substances or activities such as drugs, alcohol, sex, food, etc. The key to repaying this debt lies in cultivating adaptability, moderation, and commitment, while maintaining emotional stability and a focused approach toward achieving personal goals. People with the karmic debt number 14 must work on maintaining boundaries and self-control, avoiding destructive habits, and embracing a disciplined and balanced lifestyle to overcome their karmic challenges."
            ),
        },
        16: {
            "title": _("Abuse of love and relationships"),
            "description": _(
                "The karmic debt number 16 is associated with a strong ego and challenging relationship dynamics in past lives. Individuals with this karmic debt may struggle with failed relationships, egotism, and difficulty connecting with others. This karmic debt also represents a cycle of destruction and rebirth, often leading to significant transformations and spiritual growth. To overcome this debt, individuals must focus on humility, spiritual connection, and mindfulness, moving away from ego-driven behaviors and embracing a path of higher consciousness. It is essential to address toxic relationship patterns, foster humility, and nurture a sense of spiritual purpose to transcend the challenges associated with the karmic debt number 16."
            ),
        },
        19: {
            "title": _("Abuse of power, pride and individuality"),
            "description": _(
                "The karmic debt number 19 signifies a history of misusing power and causing suffering in past lives. Individuals with this karmic debt may exhibit traits such as selfishness, self-pride, narcissism, and an overemphasis on personal success and appearance. Consequently, they struggle to seek help or accept guidance, or acknowledge their vulnerabilities, leading to repeated instances of standing alone in the face of adversity. Their journey might be marked by an ongoing internal battle between the desire for autonomy and the necessity of support and empathy, potentially leading to a cycle of misunderstandings and isolation. This hampers their ability to forge genuine connections and hinders their personal and spiritual growth. It is crucial to let go of ego-driven behavior, embrace interdependence, and foster meaningful connections with others to navigate the challenges associated with the karmic debt number 19."
            ),
        },
    }
