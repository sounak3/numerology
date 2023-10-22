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


class CompoundNumber:

    meanings: Dict[int, Dict[str, str]] = {
        1: {
            "title": _("Not a compound number 1"),
            "description": _(
                "Not a compound number"
            ),
        },
        2: {
            "title": _("Not a compound number 2"),
            "description": _(
                "Not a compound number"
            ),
        },
        3: {
            "title": _("Not a compound number 3"),
            "description": _(
                "Not a compound number"
            ),
        },
        4: {
            "title": _("Not a compound number 4"),
            "description": _(
                "Not a compound number"
            ),
        },
        5: {
            "title": _("Not a compound number 5"),
            "description": _(
                "Not a compound number"
            ),
        },
        6: {
            "title": _("Not a compound number 6"),
            "description": _(
                "Not a compound number"
            ),
        },
        7: {
            "title": _("Not a compound number 7"),
            "description": _(
                "Not a compound number"
            ),
        },
        8: {
            "title": _("Not a compound number 8"),
            "description": _(
                "Not a compound number"
            ),
        },
        9: {
            "title": _("Not a compound number 9"),
            "description": _(
                "Not a compound number"
            ),
        },
        10: {
            "title": _("Compound number 10"),
            "description": _(
                "Symbolized as the \"Wheel of Fortune,\" it is a number of honor, faith, and self-confidence. It signifies rise and fall; one's name will be known for good or evil, according to one's desires. It is a fortunate number in the sense that one's plans are likely to be carried out."
            ),
        },
        11: {
            "title": _("Compound number 11"),
            "description": _(
                "This is an ominous number to occultists, warning of hidden dangers, trials, and treachery from others. It has the symbol of \"a Clenched Hand\" and \"a Lion Muzzled,\" indicating that the person will have great difficulties to contend against."
            ),
        },
        12: {
            "title": _("Compound number 12"),
            "description": _(
                "The symbolism of this number is suffering and anxiety of mind, often represented as \"the Sacrifice\" or \"the Victim.\" It foreshadows a scenario where one might be sacrificed for the plans or intrigues of others."
            ),
        },
        13: {
            "title": _("Compound number 13"),
            "description": _(
                "This number indicates change, not necessarily unfortunate as commonly thought. It is symbolized by \"a Skeleton\" or \"Death\" with a scythe reaping down men. It represents upheaval and destruction, along with a warning of the unknown or unexpected if it becomes a \"compound\" number in one's calculations."
            ),
        },
        14: {
            "title": _("Compound number 14"),
            "description": _(
                "This is a number of movement and combination, often accompanied by danger from natural forces such as tempests, water, air, or fire. While it can be fortunate for financial dealings and changes in business, it carries a strong element of risk and danger attached to it."
            ),
        },
        15: {
            "title": _("Compound number 15"),
            "description": _(
                "Symbolizing occult significance, this number represents magic and mystery. It indicates that the person represented by it will use every art of magic they can to carry out their purpose. Associated with a good or fortunate single number, it can be very lucky and powerful."
            ),
        },
        16: {
            "title": _("Compound number 16"),
            "description": _(
                "This number has a peculiar occult symbolism. It is represented as \"a Tower Struck by Lightning from which a man is falling with a Crown on his head,\" also known as \"the Shattered Citadel.\" It warns of strange fatality awaiting one and the danger of accidents and defeat of one’s plans."
            ),
        },
        17: {
            "title": _("Compound number 17"),
            "description": _(
                "A highly spiritual number, it is expressed symbolically by the 8-pointed Star of Venus, representing \"Peace and Love.\" It signifies that the person has risen superior in spirit to the trials and difficulties of life or their career."
            ),
        },
        18: {
            "title": _("Compound number 18"),
            "description": _(
                "This number's symbolism is difficult to translate, often pictured as \"a rayed moon from which drops of blood are falling.\" It is associated with bitter quarrels, wars, social upheavals, and revolutions. It warns of treachery, deception by others, and danger from various elements."
            ),
        },
        19: {
            "title": _("Compound number 19"),
            "description": _(
                "Symbolized as \"the Sun\" and referred to as \"the Prince of Heaven,\" this number promises happiness, success, esteem, and honor. It signifies success in one's plans for the future."
            ),
        },
        20: {
            "title": _("Compound number 20"),
            "description": _(
                "Called \"the Awakening\" or \"the Judgment,\" this number is symbolized by the figure of a winged angel sounding a trumpet. It represents the awakening of new purpose, new plans, and new ambitions, for some great cause or duty."
            ),
        },
        21: {
            "title": _("Compound number 21"),
            "description": _(
                "This number is symbolized by the picture of \"the Universe,\" also known as \"the Crown of the Magi.\" It represents advancement, honors, elevation in life, and general success, signifying victory after a long fight."
            ),
        },
        22: {
            "title": _("Compound number 22"),
            "description": _(
                "Symbolized by \"a Good Man blinded by the folly of others, with a knapsack on his back full of Errors,\" this number warns of illusion and delusion, false judgment owing to the influence of others."
            ),
        },
        23: {
            "title": _("Compound number 23"),
            "description": _(
                "Referred to as \"the Royal Star of the Lion,\" this number promises success, help from superiors, and protection from those in high places. It is considered a most fortunate number when dealing with future events."
            ),
        },
        24: {
            "title": _("Compound number 24"),
            "description": _(
                "Another fortunate number, it promises assistance and association with those of rank and position in one’s plans. It also denotes gain through love and the opposite sex."
            ),
        },
        25: {
            "title": _("Compound number 25"),
            "description": _(
                "This number denotes strength gained through experience and benefits obtained through the observation of people and things. While not deemed exactly \"lucky,\" it is favorable when it appears in relation to the future."
            ),
        },
        26: {
            "title": _("Compound number 26"),
            "description": _(
                "Full of grave warnings for the future, this number foreshadows disasters brought about by association with others, ruin through bad speculations, partnerships, unions, and bad advice."
            ),
        },
        27: {
            "title": _("Compound number 27"),
            "description": _(
                "Symbolized as \"the Sceptre,\" this number promises authority, power, and command. It indicates that rewards will come from the productive intellect and that the creative faculties have sown good seeds that will reap a harvest."
            ),
        },
        28: {
            "title": _("Compound number 28"),
            "description": _(
                "This number is full of contradictions, indicating a person of great promise and possibilities who is likely to see all taken away from him unless he carefully provides for the future. It is not fortunate for the indication of future events."
            ),
        },
        29: {
            "title": _("Compound number 29"),
            "description": _(
                "This number indicates uncertainties, treachery, and deception of others. It foreshadows trials, tribulations, and unexpected dangers, along with unreliable friends and grief caused by members of the opposite sex."
            ),
        },
        30: {
            "title": _("Compound number 30"),
            "description": _(
                "A number of thoughtful deduction and retrospection, it represents mental superiority over one’s fellows. It can be all-powerful, but it is just as often indifferent according to the will or desire of the person."
            ),
        },
        31: {
            "title": _("Compound number 31"),
            "description": _(
                "A number of thoughtful deduction, retrospection and mental superiority. This number represents a person who is even more self-contained, lonely, and isolated from his fellows. It is not a fortunate number from a worldly or material standpoint."
            ),
        },
        32: {
            "title": _("Compound number 32"),
            "description": _(
                "This number has a magical power like the single 5 or the \"compound\" numbers 14 and 23. It is usually associated with combinations of people or nations. It is a favorable number if the person it represents holds to his own judgment and opinions."
            ),
        },
        33: {
            "title": _("Compound number 33"),
            "description": _(
                "Another fortunate number, it promises assistance and association with those of rank and position in one’s plans. It also denotes gain through love and the opposite sex."
            ),
        },
        34: {
            "title": _("Compound number 34"),
            "description": _(
                "This number denotes strength gained through experience and benefits obtained through the observation of people and things. While not deemed exactly \"lucky,\" it is favorable when it appears in relation to the future."
            ),
        },
        35: {
            "title": _("Compound number 35"),
            "description": _(
                "Full of grave warnings for the future, this number foreshadows disasters brought about by association with others, ruin through bad speculations, partnerships, unions, and bad advice."
            ),
        },
        36: {
            "title": _("Compound number 36"),
            "description": _(
                "Symbolized as \"the Sceptre,\" this number promises authority, power, and command. It indicates that rewards will come from the productive intellect and that the creative faculties have sown good seeds that will reap a harvest."
            ),
        },
        37: {
            "title": _("Compound number 37"),
            "description": _(
                "This number has a distinct potency of its own. It is a number of good and fortunate friendships in love and in combinations connected with the opposite sex. It is also good for partnerships of all kinds."
            ),
        },
        38: {
            "title": _("Compound number 38"),
            "description": _(
                "This number indicates uncertainties, treachery, and deception of others. It foreshadows trials, tribulations, and unexpected dangers, along with unreliable friends and grief caused by members of the opposite sex."
            ),
        },
        39: {
            "title": _("Compound number 39"),
            "description": _(
                "A number of thoughtful deduction and retrospection, it represents mental superiority over one’s fellows. It can be all-powerful, but it is just as often indifferent according to the will or desire of the person."
            ),
        },
        40: {
            "title": _("Compound number 40"),
            "description": _(
                "A number of thoughtful deduction, retrospection and mental superiority. This number represents a person who is even more self-contained, lonely, and isolated from his fellows. It is not a fortunate number from a worldly or material standpoint."
            ),
        },
        41: {
            "title": _("Compound number 41"),
            "description": _(
                "This number has a magical power like the single 5 or the \"compound\" numbers 14 and 23. It is usually associated with combinations of people or nations. It is a favorable number if the person it represents holds to his own judgment and opinions."
            ),
        },
        42: {
            "title": _("Compound number 42"),
            "description": _(
                "Another fortunate number, it promises assistance and association with those of rank and position in one’s plans. It also denotes gain through love and the opposite sex."
            ),
        },
        43: {
            "title": _("Compound number 43"),
            "description": _(
                "This is an unfortunate number, symbolized by signs of revolution, upheaval, strife, failure, and prevention. It is not a fortunate number if it comes out in calculations relating to future events."
            ),
        },
        44: {
            "title": _("Compound number 44"),
            "description": _(
                "Full of grave warnings for the future, this number foreshadows disasters brought about by association with others, ruin through bad speculations, partnerships, unions, and bad advice."
            ),
        },
        45: {
            "title": _("Compound number 45"),
            "description": _(
                "Symbolized as \"the Sceptre,\" this number promises authority, power, and command. It indicates that rewards will come from the productive intellect and that the creative faculties have sown good seeds that will reap a harvest."
            ),
        },
        46: {
            "title": _("Compound number 46"),
            "description": _(
                "This number has a distinct potency of its own. It is a number of good and fortunate friendships in love and in combinations connected with the opposite sex. It is also good for partnerships of all kinds."
            ),
        },
        47: {
            "title": _("Compound number 47"),
            "description": _(
                "This number indicates uncertainties, treachery, and deception of others. It foreshadows trials, tribulations, and unexpected dangers, along with unreliable friends and grief caused by members of the opposite sex."
            ),
        },
        48: {
            "title": _("Compound number 48"),
            "description": _(
                "A number of thoughtful deduction and retrospection, it represents mental superiority over one’s fellows. It can be all-powerful, but it is just as often indifferent according to the will or desire of the person."
            ),
        },
        49: {
            "title": _("Compound number 49"),
            "description": _(
                "A number of thoughtful deduction, retrospection and mental superiority. This number represents a person who is even more self-contained, lonely, and isolated from his fellows. It is not a fortunate number from a worldly or material standpoint."
            ),
        },
        50: {
            "title": _("Compound number 50"),
            "description": _(
                "This number has a magical power like the single 5 or the \"compound\" numbers 14 and 23. It is usually associated with combinations of people or nations. It is a favorable number if the person it represents holds to his own judgment and opinions."
            ),
        },
        51: {
            "title": _("Compound number 51"),
            "description": _(
                "Another fortunate number, it promises assistance and association with those of rank and position in one’s plans. It also denotes gain through love and the opposite sex."
            ),
        },
        52: {
            "title": _("Compound number 52"),
            "description": _(
                "This number denotes strength gained through experience and benefits obtained through the observation of people and things. While not deemed exactly \"lucky,\" it is favorable when it appears in relation to the future."
            ),
        }
    }
