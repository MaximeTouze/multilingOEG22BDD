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

def setCurrentConfID(id):
    current_conf_id = id

def getCurrentConfID() :
    return current_conf_id

def getConfStaus(room):
    return confrence_status[room]

def startConf(room, lang, conf_id):
    confrence_status[room] = CONFRENCE_ON
    confrence_lang[room] = lang
    current_conf_id = conf_id
    initLikeSystem(room)
    initDisplayed_sentences_room(room)
    return

def setConf_questions_state(room):
    confrence_status[room] = CONFRENCE_QUESTIONS
    return

def endConf(room):
    current_conf_id = ''
    confrence_status[room] = CONFRENCE_OFF
    confrence_lang[room] = ''
    resetCache_room(room)
    return

def getLangFromRoom(room):
    print(confrence_lang, room)
    return confrence_lang[room]
