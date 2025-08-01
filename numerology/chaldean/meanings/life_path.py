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


class LifePathNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Individual action life"),
            "description": _(
                "People born under the influence of the number 1 in Cheiro's Book of Numerology are described as creative, inventive, and strongly individual. They are known for being determined and obstinate in their pursuits. This description applies to individuals born on the 1st, 10th, 19th, or 28th of any month, with heightened emphasis if they are born between the periods of the 21st July to the 28th August or the 21st March to the 28th April."
            ),
        },
        2: {
            "title": _("Life of collaboration and harmony with others"),
            "description": _(
                "Individuals influenced by the number 2 in Cheiro's Book of Numerology are characterized as gentle, imaginative, artistic, and romantic. They possess more mental than physical strength, unlike those influenced by the number 1. They are described as having a harmonious relationship with number 1 individuals, despite their contrasting characteristics."
            ),
        },
        3: {
            "title": _("Life of ambitions and expression"),
            "description": _(
                "Individuals influenced by the number 3 in Cheiro's Book of Numerology are described as ambitious, assertive, and authoritative. They are known to excel in positions of power and authority, often rising to prominent roles in various professions. Their conscientiousness and love for order and discipline contribute to their success. They find harmony with individuals born under their own number, as well as those born under 6 and 9, such as the 6th, 9th, 15th, 18th, 24th, or 27th."
            ),
        },
        4: {
            "title": _("Life of rebel and unconventionality"),
            "description": _(
                "Individuals influenced by the number 4 in Cheiro's Book of Numerology are characterized as rebellious, unconventional, and inclined to take an opposing stance in arguments. They have a natural inclination to challenge rules and regulations, often seeking to establish new orders in both personal and public life. They tend to attract a smaller circle of friends and are drawn to individuals born under the numbers 1, 2, 7, and 8."
            ),
        },
        5: {
            "title": _("Life of mobility and change"),
            "description": _(
                "Individuals influenced by the number 5 in Cheiro's Book of Numerology are described as versatile, quick-thinking, and mercurial in their characteristics. They possess an inherent craving for excitement and live on their nerves. They are known for their quick decision-making and impulsive actions, often gravitating toward methods of making money quickly, including speculative ventures such as stock market transactions."
            ),
        },
        6: {
            "title": _("A life of devotion and emotional harmony"),
            "description": _(
                "Individuals influenced by the number 6 in Cheiro's Book of Numerology are described as magnetic and capable of attracting others to them. They are often deeply loved and respected by those around them. They tend to exhibit determination and sometimes stubbornness in pursuing their plans, but their devotion to those they love is unwavering, often resembling a sense of 'mother love'. They are known for their appreciation of beauty and art, creating aesthetically pleasing environments and enjoying rich colors, paintings, statuary, and music."
            ),
        },
        7: {
            "title": _("Inner life and independence"),
            "description": _(
                "Individuals influenced by the number 7 in Cheiro's Book of Numerology are described as independent, original, and possessing a strongly marked individuality. They tend to exhibit a love for change and travel, often displaying restlessness in their nature. They are known for their philosophical outlook on life and are inclined to have a universal knowledge of the world at large. They have a strong inclination towards occultism and are often gifted with intuition and clairvoyance."
            ),
        },
        8: {
            "title": _("Life of ambitious achievements and material acquisitions"),
            "description": _(
                "Individuals influenced by the number 8 in Cheiro's Book of Numerology are often deeply misunderstood and experience intense loneliness as a result. They possess strong individuality, often playing crucial roles in the events of life, sometimes as instruments of fate for others. They exhibit determination and a zeal for causes they espouse, which can result in the development of both loyal supporters and relentless enemies."
            ),
        },
        9: {
            "title": _("Life of escape or ideal"),
            "description": _(
                "Individuals influenced by the number 9 are often described as fighters in life. Despite facing difficulties in their early years, they are ultimately successful due to their strong will, determination, and resilience. They possess an independent spirit and a quick temper, often exhibiting impulsive tendencies and a desire to be in control of their own lives. They are known for their courage and make excellent leaders or soldiers due to their fearlessness."
            ),
        },
    }
