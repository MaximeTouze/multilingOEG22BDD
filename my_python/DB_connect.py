
import mariadb
import sys

"""
def connection():
    try:
        connect = mariadb.connect(
            user = "oegadm",
            password = "oegP@ss22LS2N",
            host= "172.26.70.167",
            port=3306,
            database= "laboeg"
        )
    except mariadb.Errodef getSentence_Like_Room(room):
    return sentence_like[room]
"""
def connection():
    try:
        connect = mariadb.connect(
            user = "mysql",
            password = "oegP@ss22LS2N",
            #host= "172.26.70.167",
            host= "localhost",
            port=3306,
            database= "oeglab"
        )
    except mariadb.Error as e:
        print(f"Error while connecting to MariaDB Server:{e}")
        sys.exit(1)

    # Get the cursor
    cur = connect.cursor()

    return cur
