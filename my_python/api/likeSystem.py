from flask import jsonify
from my_python.const.lang_const import *
from my_python.DB_connect import connection

# sentence_like = {ENGLISH:{0:5, 5:2}, FRENCH:{1:5, 5:2}, ESPAGNOL:{3:5, 5:2}, ARAB:{4:5, 5:2}}

sentence_like = {}

def initLikeSystem(room) :
    language_memory = {}
    for lang in LANGUAGES :
        language_memory[lang] = {}
    sentence_like[room] = language_memory
    return

def getSentence_Like_Room(room):
    return sentence_like[room]

def getSentence_Like_Room_Lang(room, lang):
    return getSentence_Like_Room(room)[lang]

def LikeSentence(request):
    num_sentence = int(request.form.get('nb_sentence'))
    lang = request.form.get('lang')
    room = request.form.get('room')

    #cache
    try:
        #getSentence_Like_Room_Lang(room, lang)[num_sentence]+=1
        pass
    except KeyError:
        #getSentence_Like_Room_Lang(room, lang)[num_sentence]=1
        pass

    #DB

    (curr, connect) = connection()
    if lang == 'ara':

        like = curr.execute(
            "SELECT id, arabic_like FROM Likes WHERE sentence_id=?", (num_sentence,)
        )
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        try:
            like = like + 1
            curr.execute(
                "UPDATE Likes SET arabic_like=? WHERE id=?", (like, id)
            )
        except TypeError as e:
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (1, 0, 0, 0, num_sentence)
            )

    if lang == 'eng':

        like = curr.execute(
            "SELECT id, english_like FROM Likes WHERE sentence_id=?", (num_sentence,)
        )
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        try:
            like = like +1
            curr.execute(
                "UPDATE Likes SET english_like=? WHERE id=?", (like, id)
            )
        except TypeError as e:
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (0, 1, 0, 0, num_sentence)
            )


    if lang == 'fr':
        like = curr.execute(
            "SELECT id, french_like FROM Likes WHERE sentence_id=?", (num_sentence,)
        )
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        try:
            like = like +1
            curr.execute(
                "UPDATE Likes SET french_like=? WHERE id=?", (like, id)
            )
        except TypeError as e:
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (0, 0, 1, 0, num_sentence)
            )

    if lang == 'esp':
        curr.execute(
            "SELECT id, spanish_like FROM Likes WHERE sentence_id=?",(num_sentence,)
        )
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        try:
            like = like +1
            curr.execute(
                "UPDATE Likes SET spanish_like=? WHERE id=?", (like, id)
            )
        except TypeError as e:
            curr.execute(
                "INSERT INTO Likes(arabic_like , english_like , french_like , spanish_like , sentence_id) VALUES(?, ?, ?, ?, ?)",
                (0, 0, 0, 1, num_sentence)
            )
    connect.commit()
    connect.close()



def UnlikeSentence(request):
    num_sentence = int(request.form.get('nb_sentence'))
    lang = request.form.get('lang')
    room = request.form.get('room')
    print(num_sentence, lang, room)
    # cache
    #getSentence_Like_Room_Lang(room, lang)[num_sentence]-=1

    #DB
    (curr, connect) = connection()
    if lang == 'ara':
        curr.execute(
            "SELECT id, arabic_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        print ("like", like)
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
            ###
        curr.execute(
            "UPDATE Likes SET arabic_score=? WHERE id = ?", (like, id)
        )



    if lang == 'eng':
        like = curr.execute(
            "SELECT english_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        print ("like", like)
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
        curr.execute(
            "UPDATE Likes SET english_score = like WHERE sentence_id = ?", (num_sentence,)
        )




    if lang == 'fr':
        like = curr.execute(
            "SELECT french_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        print ("like", like)
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
        curr.execute(
            "UPDATE Likes SET french_score = like WHERE sentence_id =  ?", (num_sentence,)
        )



    if lang == 'esp':
        like =  curr.execute(
            "SELECT id, spanish_like FROM Likes WHERE sentence_id= ?", (num_sentence,)
        )
        like = None
        id = None
        for (id_, lik) in curr:
            like = lik
            id = id_
        print ("like", like)
        if like == 0:
            like = 0
            print('ERROR ======= MORE UNLIKE THAN LIKE :: sent = ', num_sentence, '  ;;  lang = ', lang)
        else:
            like -= 1
        connect.execute(
            "UPDATE Likes SET spanish_like=? WHERE id=?", (like, id)
        )

    connect.commit()

    connect.close()
    return


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
def Mostly_liked_sentences(room):
    result = {}
    for language in LANGUAGES:
        sentence_key_memory = -1
        sentence_like_memory = -1
        for sentence_key in getSentence_Like_Room_Lang(room, language).keys():
            if (getSentence_Like_Room_Lang(room, language)[sentence_key] > sentence_like_memory):
                sentence_like_memory = sentence_like[language][sentence_key]
                sentence_key_memory = sentence_key

        # end for
        if (sentence_key_memory != -1 and sentence_like_memory < 1):
            result[language] = {"sentence": getSentence_Like_Room_Lang(room, language)[sentence_key_memory], "nb_likes": sentence_like_memory}
        else:
            result[language] = {"sentence": "", "nb_likes": sentence_like_memory}

    result = {'liked_sentences': result}
    print("Mostly_liked_sentences", result)
    return jsonify(result)


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
