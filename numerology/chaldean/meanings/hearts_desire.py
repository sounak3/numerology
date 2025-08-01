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


class HeartsDesireNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Desire of self-achievement"),
            "description": _(
                "Number 1 individuals are characterized as ambitious and averse to restraint. They aspire to attain leadership positions in their respective fields and seek to be respected and looked up to by their subordinates. They value independence and are inclined towards taking the lead in various aspects of life."
            ),
        },
        2: {
            "title": _("Desire of collaboration"),
            "description": _(
                "Number 2 individuals are inclined towards creativity and artistry. They appreciate gentleness and often enjoy indulging in imaginative and romantic pursuits. They tend to avoid conflicts and are not as forceful in their endeavors as those born under the influence of the number 1."
            ),
        },
        3: {
            "title": _("Desire for authority"),
            "description": _(
                "Number 3 individuals strive for control and authority in their endeavors. They have a strong dislike for being in subordinate positions and are not comfortable with the idea of being obligated to others. They value their independence greatly and dislike any form of restraint."
            ),
        },
        4: {
            "title": _("Desire of social reformer"),
            "description": _(
                "Number 4 individuals are not typically focused on accumulating wealth or material possessions. They tend to utilize money in unconventional ways, surprising others with their choices. They are more inclined towards social reforms and are attracted to social issues. They are highly individualistic and value their independence."
            ),
        },
        5: {
            "title": _("Desire of excitement"),
            "description": _(
                "Number 5 individuals detest monotonous work and are inclined to pursue endeavors that offer excitement and quick rewards. They are often attracted to novel ideas and inventions that can potentially lead to financial gains. They value freedom and dislike any form of restriction or slow-paced activities."
            ),
        },
        6: {
            "title": _("Desire for emotional harmony"),
            "description": _(
                "Number 6 individuals are inclined towards creating harmonious environments and fostering love and happiness among their friends and family. They dislike discord and jealousy, often striving to maintain a peaceful and loving atmosphere. They appreciate generosity and are often willing to go to great lengths to support causes they believe in or people they deeply care about."
            ),
        },
        7: {
            "title": _("Desire of inner wisdom"),
            "description": _(
                "Number 7 individuals tend to cherish the desire for exploration and travel, often immersing themselves in literature on far-off lands. They often hold a disinterest in material possessions, with a willingness to make significant donations to charitable causes if they attain wealth. They have a unique religious inclination, preferring to create their own form of spirituality that appeals to their imaginative and mysterious nature."
            ),
        },
        8: {
            "title": _("Desire of material success"),
            "description": _(
                "Number 8 individuals are driven by an extreme devotion to the causes they take up, and they tend to be fanatical in their approach. While they often appear cold and reserved, they harbor warm feelings for the oppressed and downtrodden. They are prone to extremism in their religious or spiritual beliefs and dislike being misunderstood."
            ),
        },
        9: {
            "title": _("Desire of recognition of efforts"),
            "description": _(
                "Number 9 individuals desire recognition and appreciation for their efforts. They prefer to be seen as the head of the household and do not take well to criticism or interference. They value affection and sympathy and are capable of significant sacrifices for their loved ones. They are drawn to people whose birth dates fall in the series of 3, 6, or 9, as these numbers resonate harmoniously with their own vibration."
            ),
        },
    }
