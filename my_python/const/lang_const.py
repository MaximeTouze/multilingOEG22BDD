# front languages
# english code
ENGLISH = "eng"
# french code
FRENCH = "fr"
# spanish code
ESPAGNOL = "esp"
# arabic code
ARAB = "ara"

# List of languages
LANGUAGES = [ENGLISH, FRENCH, ESPAGNOL, ARAB]

# transcription languages
# Eglish for transcription
TRANS_ENGLISH = "en-US"
# French for transcription
TRANS_FRENCH = "fr-FR"
# Spanish for transcription
TRANS_SPANISH = "es-ES"
# Arabic for transcription
TRANS_ARAB = "ar-DZ"

# List of transcription languages
TRANS_LANGUAGES = [TRANS_ENGLISH, TRANS_FRENCH, TRANS_SPANISH, TRANS_ARAB]

# Traduction languages
# English for traduction
TRAD_ENGLISH = "english"
# French for traduction
TRAD_FRENCH = "french"
# Spanish for traduction
TRAD_SPANISH = "spanish"
# Arabic for traduction
TRAD_ARAB = "arabic"

# List of traduction languages
TRAD_LANGUAGES = [TRAD_ENGLISH, TRAD_FRENCH, TRAD_SPANISH, TRAD_ARAB]

# Transcription key
TRANS = "trans"
# Traduction key
TRAD = "trad"

# The dictionnary for getting the transcription an traduction languages from the front lanuage as :
# {
#   front language :
#   {
#       key (trans or trad) : language
#   }
# }
LANGUAGES_MATCHER = {}
for i in range (0, len(TRAD_LANGUAGES), 1):
    LANGUAGES_MATCHER[LANGUAGES[i]] = {TRANS : TRANS_LANGUAGES[i], TRAD : TRAD_LANGUAGES[i]}

# gives the front language from the traduction one
REVERSE_MATCHER = {TRAD_ENGLISH: ENGLISH, TRAD_FRENCH: FRENCH, TRAD_SPANISH: ESPAGNOL, TRAD_ARAB: ARAB}
