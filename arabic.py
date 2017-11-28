"""This module contains Arabic tools for text analysis
"""

# Constans.
COMMA            = u'\u060C'
SEMICOLON        = u'\u061B'
QUESTION         = u'\u061F'
HAMZA            = u'\u0621'
ALEF_MADDA       = u'\u0622'
ALEF_HAMZA_ABOVE = u'\u0623'
WAW_HAMZA        = u'\u0624'
ALEF_HAMZA_BELOW = u'\u0625'
YEH_HAMZA        = u'\u0626'
ALEF             = u'\u0627'
BEH              = u'\u0628'
TEH_MARBUTA      = u'\u0629'
TEH              = u'\u062a'
THEH             = u'\u062b'
JEEM             = u'\u062c'
HAH              = u'\u062d'
KHAH             = u'\u062e'
DAL              = u'\u062f'
THAL             = u'\u0630'
REH              = u'\u0631'
ZAIN             = u'\u0632'
SEEN             = u'\u0633'
SHEEN            = u'\u0634'
SAD              = u'\u0635'
DAD              = u'\u0636'
TAH              = u'\u0637'
ZAH              = u'\u0638'
AIN              = u'\u0639'
GHAIN            = u'\u063a'
TATWEEL          = u'\u0640'
FEH              = u'\u0641'
QAF              = u'\u0642'
KAF              = u'\u0643'
LAM              = u'\u0644'
MEEM             = u'\u0645'
NOON             = u'\u0646'
HEH              = u'\u0647'
WAW              = u'\u0648'
ALEF_MAKSURA     = u'\u0649'
YEH              = u'\u064a'
MADDA_ABOVE      = u'\u0653'
HAMZA_ABOVE      = u'\u0654'
HAMZA_BELOW      = u'\u0655'
ZERO             = u'\u0660'
ONE              = u'\u0661'
TWO              = u'\u0662'
THREE            = u'\u0663'
FOUR             = u'\u0664'
FIVE             = u'\u0665'
SIX              = u'\u0666'
SEVEN            = u'\u0667'
EIGHT            = u'\u0668'
NINE             = u'\u0669'
PERCENT          = u'\u066a'
DECIMAL          = u'\u066b'
THOUSANDS        = u'\u066c'
STAR             = u'\u066d'
MINI_ALEF        = u'\u0670'
ALEF_WASLA       = u'\u0671'
FULL_STOP        = u'\u06d4'
BYTE_ORDER_MARK  = u'\ufeff'

# Diacritics
FATHATAN         = u'\u064b'
DAMMATAN         = u'\u064c'
KASRATAN         = u'\u064d'
FATHA            = u'\u064e'
DAMMA            = u'\u064f'
KASRA            = u'\u0650'
SHADDA           = u'\u0651'
SUKUN            = u'\u0652'

# Small Letters
SMALL_ALEF       = u"\u0670"
SMALL_WAW        = u"\u06E5"
SMALL_YEH        = u"\u06E6"
#Ligatures
LAM_ALEF                     = u'\ufefb'
LAM_ALEF_HAMZA_ABOVE         = u'\ufef7'
LAM_ALEF_HAMZA_BELOW         = u'\ufef9'
LAM_ALEF_MADDA_ABOVE         = u'\ufef5'
SIMPLE_LAM_ALEF              = u'\u0644\u0627'
SIMPLE_LAM_ALEF_HAMZA_ABOVE  = u'\u0644\u0623'
SIMPLE_LAM_ALEF_HAMZA_BELOW  = u'\u0644\u0625'
SIMPLE_LAM_ALEF_MADDA_ABOVE  = u'\u0644\u0622'
# groups
LETTERS = u''.join([
        ALEF, 
        BEH,
        TEH,
        THEH,
        JEEM,  
        HAH,  
        KHAH, 
        DAL,
        THAL,
        REH,  
        ZAIN,  
        SEEN, 
        SHEEN,  
        SAD,  
        DAD,  
        TAH, 
        ZAH, 
        AIN,
        GHAIN,  
        FEH,  
        QAF,  
        KAF, 
        LAM,  
        MEEM,  
        NOON,  
        HEH,  
        WAW,  
        YEH, 
        HAMZA,   
        ALEF_MADDA,  
        ALEF_HAMZA_ABOVE,  
        WAW_HAMZA,  
        ALEF_HAMZA_BELOW,
        YEH_HAMZA, 
        ALEF_MAKSURA,  
        TEH_MARBUTA
        ])

TASHKEEL  = (FATHATAN,  DAMMATAN,  KASRATAN, 
            FATHA, DAMMA, KASRA, 
            SUKUN, 
            SHADDA)
HARAKAT  = (  FATHATAN,    DAMMATAN,    KASRATAN, 
            FATHA,   DAMMA,   KASRA, 
            SUKUN
            )
SHORTHARAKAT  = ( FATHA,   DAMMA,   KASRA,  SUKUN)

TANWIN  = (FATHATAN,   DAMMATAN,    KASRATAN)

NOT_DEF_HARAKA = TATWEEL
LIGUATURES = (
            LAM_ALEF, 
            LAM_ALEF_HAMZA_ABOVE, 
            LAM_ALEF_HAMZA_BELOW, 
            LAM_ALEF_MADDA_ABOVE, 
            )
HAMZAT = (
            HAMZA, 
            WAW_HAMZA, 
            YEH_HAMZA, 
            HAMZA_ABOVE, 
            HAMZA_BELOW, 
            ALEF_HAMZA_BELOW, 
            ALEF_HAMZA_ABOVE, 
            )
ALEFAT = (
            ALEF, 
            ALEF_MADDA, 
            ALEF_HAMZA_ABOVE, 
            ALEF_HAMZA_BELOW, 
            ALEF_WASLA, 
            ALEF_MAKSURA, 
            SMALL_ALEF, 

        )
WEAK   = ( ALEF,  WAW,  YEH,  ALEF_MAKSURA)
YEHLIKE =  ( YEH,   YEH_HAMZA,   ALEF_MAKSURA,    SMALL_YEH  )

WAWLIKE   = ( WAW,   WAW_HAMZA,   SMALL_WAW )
TEHLIKE   = ( TEH,   TEH_MARBUTA )

SMALL   = ( SMALL_ALEF,  SMALL_WAW,  SMALL_YEH)
MOON = (HAMZA            , 
        ALEF_MADDA       , 
        ALEF_HAMZA_ABOVE , 
        ALEF_HAMZA_BELOW , 
        ALEF             , 
        BEH              , 
        JEEM             , 
        HAH              , 
        KHAH             , 
        AIN              , 
        GHAIN            , 
        FEH              , 
        QAF              , 
        KAF              , 
        MEEM             , 
        HEH              , 
        WAW              , 
        YEH
    )
SUN = (
        TEH              , 
        THEH             , 
        DAL              , 
        THAL             , 
        REH              , 
        ZAIN             , 
        SEEN             , 
        SHEEN            , 
        SAD              , 
        DAD              , 
        TAH              , 
        ZAH              , 
        LAM              , 
        NOON             , 
    )
ALPHABETIC_ORDER = {
                ALEF             : 1, 
                BEH              : 2, 
                TEH              : 3, 
                TEH_MARBUTA      : 3, 
                THEH             : 4, 
                JEEM             : 5, 
                HAH              : 6, 
                KHAH             : 7, 
                DAL              : 8, 
                THAL             : 9, 
                REH              : 10, 
                ZAIN             : 11, 
                SEEN             : 12, 
                SHEEN            : 13, 
                SAD              : 14, 
                DAD              : 15, 
                TAH              : 16, 
                ZAH              : 17, 
                AIN              : 18, 
                GHAIN            : 19, 
                FEH              : 20, 
                QAF              : 21, 
                KAF              : 22, 
                LAM              : 23, 
                MEEM             : 24, 
                NOON             : 25, 
                HEH              : 26, 
                WAW              : 27, 
                YEH              : 28, 
                HAMZA            : 29, 
                ALEF_MADDA       : 29, 
                ALEF_HAMZA_ABOVE : 29, 
                WAW_HAMZA        : 29, 
                ALEF_HAMZA_BELOW : 29, 
                YEH_HAMZA        : 29, 
                }


"""
    * Some alphabet building tools
"""
def alphabet_excluding(excludedLetters):
    """returns the alphabet excluding the given letters.

    Args:
        excludedLetters (list['char']): letters to be excluded from the alphabet

    Returns:
        str: alphabet excluding the given excludedLetters

    Calling:
        `print(alphabet_excluding([TAH, SHEEN, ZAIN, THAL, YEH]))`
        
    """
    filtered_alphabet = ''
    for letter in excludedLetters:
        filtered_alphabet = LETTERS.replace(letter, '') 
    return filtered_alphabet
