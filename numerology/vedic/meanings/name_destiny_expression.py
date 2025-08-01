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


class DestinyNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Born to lead"),
            "description": _(
                "According to the text, number 1 individuals are likely to succeed in their endeavors, particularly when they align their actions with their own number or during specific periods, such as from 21st July to 28th August, and from 21st March to 28th April. They are likely to find harmony and success in relationships with individuals born under the influence of the numbers 2, 4, and 7."
            ),
        },
        2: {
            "title": _("Born to bring harmony"),
            "description": _(
                "According to the text, number 2 individuals are advised to carry out their main plans and ideas during specific periods, especially from the 20th June to the 27th July. They resonate well with individuals born under the influence of numbers 1 and 7, finding harmonious relationships with them."
            ),
        },
        3: {
            "title": _("Born to manage"),
            "description": _(
                "Number 3 individuals are advised to carry out their plans and aims on specific dates that vibrate with the number 3, such as the 3rd, 12th, 21st, and 30th of any month, especially during the periods of February 19th to March 20th-27th, and November 21st to December 20th-27th. They are known to be successful in roles that require trust and responsibility due to their conscientious and commanding nature."
            ),
        },
        4: {
            "title": _("Born to stabilize"),
            "description": _(
                "Number 4 individuals are advised to implement their plans and ideas on dates that resonate with their number, such as the 4th, 13th, 22nd, and 31st of any month, especially during the periods from June 21st to July 20th-27th, and from July 22nd to the end of August. They might not achieve as much success in worldly or material matters as those born under other numbers."
            ),
        },
        5: {
            "title": _("Born to change"),
            "description": _(
                "Number 5 individuals are known for their remarkable resilience and the ability to quickly recover from setbacks. They tend to rebound from adversity swiftly, exhibiting a remarkable elasticity of character. They are often inclined towards speculative ventures and may find success in endeavors that require quick thinking and risk-taking."
            ),
        },
        6: {
            "title": _("Born for caring"),
            "description": _(
                "Number 6 individuals are known for their ability to make a wide circle of friends, particularly with individuals born under the vibrations of 3, 6, and 9, or their respective series. They are considered fortunate on Tuesdays, Thursdays, and Fridays, especially if these days coincide with their own number or the numbers 3, 6, or 9.  They are advised to carry out their plans and aims on dates that fall under their own number, especially during the periods from April 20th to May 20th-27th, and from September 21st to October 20th-27th."
            ),
        },
        7: {
            "title": _("Born to have inner wisdom"),
            "description": _(
                "Number 7 individuals are likely to be successful in fields that involve exploration, travel, or intellectual pursuits. They might excel in writing, painting, or poetry, incorporating their philosophical perspectives into their creative works. They may also find success in businesses related to foreign trade or shipping if given the opportunity. They are advised to carry out their plans and aims on dates that fall under their own number, especially during the period from June 21st to July 20th-27th, and to prioritize Sundays and Mondays for important decisions."
            ),
        },
        8: {
            "title": _("Born to achieve"),
            "description": _(
                "Number 8 individuals tend to experience extreme highs and lows in their lives. They may achieve great success or face significant failures, with little middle ground. They are often associated with sacrifices and are called upon to endure profound sorrows, losses, and humiliations. The path of those influenced by the number 8 is fraught with challenges and obstacles, often resulting in tragic endings. They are advised to execute their plans on days falling under their own number, primarily on Saturdays, Sundays, and Mondays, or any other days that correspond with their interchangeable number 4."
            ),
        },
        9: {
            "title": _("Born to overcome struggles"),
            "description": _(
                "Individuals influenced by the number 9 often experience conflict and strife, both in their personal relationships and in their endeavors. They are susceptible to accidents, especially those related to fire and explosions, and frequently undergo surgical operations. Despite the challenges they face, they display a strong determination and a willingness to overcome obstacles, ultimately achieving success through their relentless efforts. They are are advised to exercise control over their fiery temperaments and impulsive tendencies. Developing patience and a more measured approach to decision-making can help them navigate life's challenges more smoothly."
            ),
        },
    }
