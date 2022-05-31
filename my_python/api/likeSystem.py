from flask import jsonify
from my_python.const.lang_const import *
from my_python.DB_connect import connection

import my_python.const.lang_const as LangConst
import mariadb
from flask_caching import Cache

sentence_like = {}

# init the like system for the griven room
def initLikeSystem(room) :
    language_memory = {}
    for lang in LANGUAGES :
        language_memory[lang] = {}
    sentence_like[room] = language_memory
    return

# returns the likes for the room
def getSentence_Like_Room(room):
    return sentence_like[room]

# returns the likes from a room and a language
def getSentence_Like_Room_Lang(room, lang):
    return getSentence_Like_Room(room)[lang]

# Like a sentencefrom the request
def LikeSentence(request):
    num_sentence = int(request.form.get('nb_sentence'))
    lang = request.form.get('lang')
    room = request.form.get('room')

    #DB

    (curr, connect) = connection()
    # in case the language is Arabic
    if lang == 'ara':
        # getting the current likes amount
        curr.execute(
            "SELECT id, arabic_like FROM Likes WHERE sentence_id=?", (num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # increment likes coounter
        try:
            like = like + 1
            # update like amount
            curr.execute(
                "UPDATE Likes SET arabic_like=? WHERE id=?", (like, id)
            )
        # if error : no like exists
        except TypeError as e:
            # create like line in DB
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (1, 0, 0, 0, num_sentence)
            )

    # In case the language is english
    if lang == 'eng':
        # getting the current likes amount
        curr.execute(
            "SELECT id, english_like FROM Likes WHERE sentence_id=?", (num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # increment likes coounter
        try:
            like = like +1
            # update like amount
            curr.execute(
                "UPDATE Likes SET english_like=? WHERE id=?", (like, id)
            )
        # if error : no like exists
        except TypeError as e:
            # create like line in DB
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (0, 1, 0, 0, num_sentence)
            )

    # in case the language is frensh
    if lang == 'fr':
        # getting the current likes amount
        curr.execute(
            "SELECT id, french_like FROM Likes WHERE sentence_id=?", (num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # increment likes coounter
        try:
            like = like +1
            # update like amount
            curr.execute(
                "UPDATE Likes SET french_like=? WHERE id=?", (like, id)
            )
        # if error : no like exists
        except TypeError as e:
            # create like line in DB
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (0, 0, 1, 0, num_sentence)
            )

    # in case the language is spanish
    if lang == 'esp':
        # getting the current likes amount
        curr.execute(
            "SELECT id, spanish_like FROM Likes WHERE sentence_id=?",(num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # increment likes coounter
        try:
            like = like +1
            # update like amount
            curr.execute(
                "UPDATE Likes SET spanish_like=? WHERE id=?", (like, id)
            )
        # if error : no like exists
        except TypeError as e:
            # create like line in DB
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (0, 0, 0, 1, num_sentence)
            )
    connect.commit()
    connect.close()


# Unlike a sentence
def UnlikeSentence(request):
    num_sentence = int(request.form.get('nb_sentence'))
    lang = request.form.get('lang')
    room = request.form.get('room')

    #DB
    (curr, connect) = connection()
    # in case the language is arabic
    if lang == 'ara':
        # getting the current likes amount
        curr.execute(
            "SELECT id, arabic_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # in case there is 0 likes
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
        # update like amount
        curr.execute(
            "UPDATE Likes SET arabic_like=? WHERE id = ?", (like, id)
        )


    # in case the language is english
    if lang == 'eng':
        # getting the current likes amount
        curr.execute(
            "SELECT id, english_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # in case there is 0 likes
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
        curr.execute(
            "UPDATE Likes SET english_like=? WHERE id=?", (like, id)
        )



    # in case the language is french
    if lang == 'fr':
        # getting the current likes amount
        curr.execute(
            "SELECT id, french_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # in case there is 0 likes
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
        # update like amount
        curr.execute(
            "UPDATE Likes SET french_like=? WHERE id=?", (like, id)
        )


    # in case the language is spanish
    if lang == 'esp':
        # getting the current likes amount
        curr.execute(
            "SELECT id, spanish_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        # getting like and id :
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        # in case there is 0 likes
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
        # update like amount
        curr.execute(
            "UPDATE Likes SET spanish_like=? WHERE id=?", (like, id)
        )

    connect.commit()

    connect.close()
    return



##################### For one conf ##############################################


# returns the most liked sentence for each language
#{
# 'liked_sentences':
# {
#  "language name" :
#  {
#      "sentence" : "the most liked sentence"
#      "nb_likes" : likes_nuber
#  }
# }
#}

def Mostly_liked_sentences(room, conf_id):
    result = {}

    (curr, connect) = connection()
    # if there is a conf id
    if (conf_id != None and conf_id != ''):
        print(conf_id)
        try:
            # getting all the mostyl liked sentences
            result[LangConst.ENGLISH] = getEngMostlyLiked(curr, conf_id)
            result[LangConst.FRENCH] = getFrMostlyLiked(curr, conf_id)
            result[LangConst.ESPAGNOL] = getEspMostlyLiked(curr, conf_id)
            result[LangConst.ARAB] = getArabMostlyLiked(curr, conf_id)

        except mariadb.Error as e:
            print(f"Error: {e}")
        connect.close()

        result = {"liked_sentences": result}
        print("Mostly_liked_sentences", result)
        return result
    else :
        print("!!! NO CONF ID !!!")

# Returns the most liked sentence for arabic
def getArabMostlyLiked(curr, conf_id):
    # getting the mostly kiled sentence
    curr.execute(
        "SELECT Sentence.arabic, Likes.arabic_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Sentence.conf_id=? AND Likes.arabic_like = (SELECT MAX(Likes.arabic_like) FROM Likes)", (conf_id,)
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence": sent, "nb_likes": likes}
    return {"sentence": "No arabic liked sentence found", "nb_likes": ""}

# Returns the most liked sentence for english
def getEngMostlyLiked(curr, conf_id):
    # getting the mostly kiled sentence
    curr.execute(
        "SELECT Sentence.english, Likes.english_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Sentence.conf_id=? AND Likes.english_like = (SELECT MAX(Likes.english_like) FROM Likes)", (conf_id,)
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence": sent, "nb_likes": likes}
    return {"sentence": "No english liked sentence found", "nb_likes": ""}

# Returns the most liked sentence for french
def getFrMostlyLiked(curr, conf_id):
    # getting the mostly kiled sentence
    curr.execute(
        "SELECT Sentence.french, Likes.french_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Sentence.conf_id=? AND Likes.french_like  = (SELECT MAX(Likes.french_like) FROM Likes)", (conf_id,)
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence": sent, "nb_likes": likes}
    return {"sentence": "No french liked sentence found", "nb_likes": ""}

# Returns the most liked sentence for spanish
def getEspMostlyLiked(curr, conf_id):
    # getting the mostly kiled sentence
    curr.execute(
        "SELECT Sentence.spanish, Likes.spanish_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Sentence.conf_id=? AND Likes.spanish_like = (SELECT MAX(Likes.spanish_like) FROM Likes)", (conf_id,)
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence":sent, "nb_likes": likes}
    return {"sentence": "No espagnol liked sentence found", "nb_likes": ""}


############################## TOTAL ########################################

# returns the most liked sentence for each language for all the conferences
#{
# 'liked_sentences':
# {
#  "language name" :
#  {
#      "sentence" : "the most liked sentence"
#      "nb_likes" : likes_nuber
#  }
# }
#}
def Mostly_liked_sentences_total(room):
    result = {}

    (curr, connect) = connection()
    # if there is a conf id
    try:
        # getting all the mostyl liked sentences
        result[LangConst.ENGLISH] = getEngMostlyLiked_total(curr)
        result[LangConst.FRENCH] = getFrMostlyLiked_total(curr)
        result[LangConst.ESPAGNOL] = getEspMostlyLiked_total(curr)
        result[LangConst.ARAB] = getArabMostlyLiked_total(curr)

    except mariadb.Error as e:
        print(f"Error: {e}")
    connect.close()

    result = {"liked_sentences": result}
    print("Mostly_liked_sentences", result)
    return result


# Returns the most liked sentence for arabic for all the confereces
def getArabMostlyLiked_total(curr):
    # getting the mostly kiled sentence
    curr.execute(

        "SELECT Sentence.arabic, Likes.arabic_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Likes.arabic_like = (SELECT MAX(Likes.arabic_like) FROM Likes)"
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence": sent, "nb_likes": likes}
    return {"sentence": "No arabic liked sentence found", "nb_likes": ""}

# Returns the most liked sentence for english for all the confereces
def getEngMostlyLiked_total(curr):
    # getting the mostly kiled sentence
    curr.execute(
        "SELECT Sentence.english, Likes.english_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Likes.english_like = (SELECT MAX(Likes.english_like) FROM Likes)"
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence": sent, "nb_likes": likes}
    return {"sentence": "No english liked sentence found", "nb_likes": ""}

# Returns the most liked sentence for french for all the confereces
def getFrMostlyLiked_total(curr):
    # getting the mostly kiled sentence
    curr.execute(
        "SELECT Sentence.french, Likes.french_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Likes.french_like  = (SELECT MAX(Likes.french_like) FROM Likes)"
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence": sent, "nb_likes": likes}
    return {"sentence": "No french liked sentence found", "nb_likes": ""}

# Returns the most liked sentence for spanish for all the confereces
def getEspMostlyLiked_total(curr):
    # getting the mostly kiled sentence
    curr.execute(
        "SELECT Sentence.spanish, Likes.spanish_like FROM Sentence INNER JOIN Likes ON Sentence.id = Likes.sentence_id WHERE Likes.spanish_like = (SELECT MAX(Likes.spanish_like) FROM Likes)"
    )
    # preparing the result
    for (sent, likes) in curr:
        return {"sentence":sent, "nb_likes": likes}
    return {"sentence": "No espagnol liked sentence found", "nb_likes": ""}




###############################################################
# Place the tab rank value to the tab rank-1
# WARN Does not change the given rank value, you have to do it
def MoveDownValues(sentences_rank_result, sentences_count_result, count_result_rank):
    if (count_result_rank < 1):
        return (sentences_rank_result, sentences_count_result)
    else :
        (new_sentences_rank_result, new_sentences_count_result) = MoveDownValues(sentences_rank_result, sentences_count_result, count_result_rank-1)
        new_sentences_rank_result[count_result_rank-1] = new_sentences_rank_result[count_result_rank]
        new_sentences_count_result[count_result_rank-1] = new_sentences_count_result[count_result_rank]
        return (new_sentences_rank_result, new_sentences_count_result)
