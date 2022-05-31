# Manage conf status

from my_python.manager.cache_data_manager import initDisplayed_sentences_room, resetCache_room
from my_python.api.likeSystem import initLikeSystem


# Consts
CONFRENCE_ON = 1
CONFRENCE_QUESTIONS = 0
CONFRENCE_OFF = -1

current_conf_id = ""

# Globals
confrence_status = {}
confrence_lang = {}

# Change the conference ID by the ID gave as param
def setCurrentConfID(id):
    current_conf_id = id

# Returns the current conf ID
def getCurrentConfID() :
    return current_conf_id

# Return the conference status from the room
def getConfStaus(room):
    return confrence_status[room]

# Starts the conference from the room, the language and the conf_id
def startConf(room, lang, conf_id):
    confrence_status[room] = CONFRENCE_ON
    confrence_lang[room] = lang
    current_conf_id = conf_id
    # initialize the like system
    initLikeSystem(room)
    # init the sentences displayed for the room
    initDisplayed_sentences_room(room)
    return

# Put the conference to question state
def setConf_questions_state(room):
    confrence_status[room] = CONFRENCE_QUESTIONS
    return

# Finishes the conference
def endConf(room):
    current_conf_id = ''
    confrence_status[room] = CONFRENCE_OFF
    confrence_lang[room] = ''
    # reset the cache for the room
    resetCache_room(room)
    return

# Returns the current talked language for the given room
def getLangFromRoom(room):
    print(confrence_lang, room)
    return confrence_lang[room]
