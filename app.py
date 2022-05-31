from flask import Flask, render_template, request, jsonify
from urllib.request import urlretrieve
import wave, struct
import json
#import js2py
#import re
import mariadb
import requests
import os as os

import base64


from datetime import datetime

import my_python.api.conf_manager as ConfManager
import my_python.manager.cache_data_manager as CacheDataManager
import my_python.api.likeSystem as likeSystem
from my_python.DB_connect import connection
import my_python.const.lang_const as LangConst
from flask_caching import Cache

# Flask init
app = Flask(__name__, template_folder='templates')

# Cache init
cache = Cache(app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp'})

######################## The app's Views ########################

## Welcome page ::
@app.route('/')
def root():
    return render_template('index.html')


## Tutorial page ::
@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


## The app's html view ::
@app.route('/view')
def view():
    print("=== view asked ===")
    # getting conf title
    r = requests.get("https://multiling-oeg.univ-nantes.fr/confTitle")
    content = json.loads(r.content)
    #print(content)
    if(r.status_code == 200 and content["title"] != ""):
        return render_template('view.html', title=content["title"][0])
    else :
        return render_template('view.html', title=None)

# The app's html view with auto changes for language
@app.route('/view_auto')
def view_auto():
    # getting conf title
    r = requests.get("https://multiling-oeg.univ-nantes.fr/confTitle")
    content = json.loads(r.content)
    if(r.status_code == 200 and content["title"] != ""):
        return render_template('view.html', title=content["title"][0], auto=True)
    else :
        return render_template('view.html', title=None, auto=True)


# A route for testing
@app.route('/view_test')
def view_test():
    return render_template('view.html')


############ Results Pages ############
# Returns the results page of the likes from the current conference (WIP)
@app.route("/results")
def ResultsPage():
    results= likeSystem.Mostly_liked_sentences(1, cache.get("current_conf_id"))
    return render_template('results.html', result= results)


# Returns the results page of the likes from the entire DB
@app.route("/total_results")
def ResultsPageTotal():
    results= likeSystem.Mostly_liked_sentences_total(1)
    return render_template('results.html', result= results)


############ Tool pages ###############
# Returns the page showing the QR to the view
@app.route("/qr")
def QR_page():
    return render_template('qr.html')


######################## The app's APIs ########################
# Deprecated API
@app.route("/update", methods=['POST'])
def update():
    text = request.form['text']
    language = request.form['lang']
    return render_template('record.html')


# Returns the sentences
@app.route("/sentences", methods=['GET'])
def sentences():
    print("=== sentences asked ===")

    num_sentence = int(request.args.get('nb_sentence'))
    room = int(request.args.get('room'))
    lang = request.args.get('lang')

    # Get from the database
    (curr, connect) = connection()

    curr.execute(
        # SELECT THE LAST 3 SENTENCES
        "SELECT id, english, french, spanish, arabic FROM Sentence ORDER BY id DESC LIMIT 1"
    )

    sent = {}
    for (id, english, french, spanish, arabic) in curr:
      if(lang == LangConst.ARAB):
        sent[id] = arabic
      elif (lang == LangConst.ENGLISH):
        sent[id] = english
      elif (lang == LangConst.FRENCH):
        sent[id] = french
      elif (lang == LangConst.ESPAGNOL):
        sent[id] = spanish

    connect.close()
    return jsonify({'sentences': sent})




############ Likes system ############

# Add a like to a sentence
@app.route("/likeSentence", methods=['POST'])
def LikeSentence():
    print("=== one more like ===")
    likeSystem.LikeSentence(request)
    return render_template('view.html')

# Remove a like to a sentence
@app.route("/UnlikeSentence", methods=['POST'])
def UnlikeSentence():
    print("=== one less like ===")
    likeSystem.UnlikeSentence(request)
    return render_template('view.html')


# returns the most liked sentence for each language
#{
# "sentences":
#   {
#    'liked_sentences':
#    [{
#     "language name" :
#      {
#         "sentence" : "the most liked sentence"
#         "nb_likes" : likes_nuber
#      }
#    }]
#   }
#}
@app.route("/mostly_liked_sentences", methods=['GET'])
def Mostly_liked_sentences_api():
    mostly_liked_sentences = likeSystem.Mostly_liked_sentences(1, cache)
    return jsonify({'sentences': mostly_liked_sentences}), 400


############ Conf Management ############

# Starts the new conference
@app.route("/startConf", methods=['POST'])
def startConf():
    room = int(request.form.get('room'))
    lang = request.form.get('lang')
    conf_id = request.form.get('conf_id')
    ConfManager.startConf(room, lang, conf_id)
    return render_template('index.html')

# Stop the conference (recording)
@app.route("/stopConf", methods=['POST'])
def stopConf():
    room = int(request.form.get('room'))
    ConfManager.setConf_questions_state(room)
    return render_template('index.html')

# Finish the conference
@app.route("/endConf", methods=['POST'])
def endConf():
    room = int(request.form.get('room'))
    ConfManager.endConf(room)
    return render_template('index.html')


# Update the wordclouds from the form as images (must be a dictionnary as {"key":picture})
# Images must look like :
# {
#   "english": "the english WC",
#   "french": "the frensh WC",
#   "spanish": "the spanish WC"
#   "arabic": "the arabic WC"
# }
@app.route("/updateWordCloud", methods=['POST'])
def updateWordCloud():
    print("=== new WordCloud ===")

    values = request.form
    # the path for hosting the word cloud
    path = "/var/www/html/multilingOEG22/static/exposed" #hosted

    # for each language and img couple
    for k,v in values.items():
        decoded = base64.b64decode(v)
        lang = LangConst.REVERSE_MATCHER[k]
        image_result = open(f'{path}/word_cloud.{lang}.png', 'wb')
        image_result.write(decoded)
        image_result.close()

    return render_template('index.html')



# Insert sentences from request datas :
# Parameters must looking like
# {     # conference informations
#   "conf_id": conf_id,
#   "conf_name": conf_name,
#   "conf_room": room_of_the_conference,
#   "sentences": {
#       "english": "the english sentence",
#       "french": "the frensh sentence",
#       "spanish": "the spanish sentence"
#       "arabic": "the arabic sentence"
#   }
#}
@app.route("/insertion", methods=['POST'])
def SentenceInsertion():
    print("=== new sentence ===")
    values = request.data
    # Bytes to JSon
    values = values.decode('utf8')


    # Json to dictionnary
    values = json.loads(values)

    # Conference informations
    conf_id = values['conf_id']
    conf_name = values['conf_name']
    conf_room = values['conf_room']
    conf_lang = values['conf_lang']

    # Sentences content
    eng_sentence = values['sentences'][LangConst.TRAD_ENGLISH]
    fr_sentence = values['sentences'][LangConst.TRAD_FRENCH]
    esp_sentence = values['sentences'][LangConst.TRAD_SPANISH]
    ara_sentence = values['sentences'][LangConst.TRAD_ARAB]


    # Database insertion
    (curr, connect) = connection()
    cache.set("current_conf_id", conf_id)

    # Conference
    conf_id = conf_id
    conferenceTitle = conf_name
    langue = conf_lang

    # Sentence
    english = eng_sentence
    french = fr_sentence
    spanish = esp_sentence
    arabic = ara_sentence

    conf_id = conf_id

    # Trying to insert a new conference in the DB
    try:
        curr.execute(
            "INSERT INTO Conference(id, conferenceTitle, langue) VALUES(?, ?, ?)",
            (conf_id, conferenceTitle, langue)
        )
        connect.commit()
    except mariadb.Error as e:
        print(f"DB Error: {e}")

    # Tring to insert new sentence in DB
    try:
        curr.execute(
            "INSERT INTO Sentence(english, french, spanish, arabic, conf_id) VALUES(?, ?, ?, ?, ?)",
            (english, french, spanish, arabic, conf_id)
        )
        connect.commit()
    except mariadb.Error as e:
        print(f"DB Error: {e}")



    # Close the database connection
    connect.close()
    return jsonify({'status_code': '200'})


# Returns the conference title
# Result : {"title": title}
@app.route("/confTitle", methods=['GET'])
def GetConfTitle():
    # getting the id of the current coference
    conf_id = cache.get("current_conf_id")
    (curr, connect) = connection()
    curr.execute(
     "SELECT conferenceTitle from Conference where id = ?", (conf_id,)
    )
    res = ""
    # Get the result from the DB request
    for confTitle in curr:
        res = confTitle
    connect.close()
    return jsonify({'title': res})




if __name__== '__main__':
    app.run()
