
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
# connect to the DB : return the connection and the cursor
def connection():
    try:
        connect = mariadb.connect(
            user = "root",
            password = "oegP@ss22LS2N",
            database= "oeglab"
        )
    except mariadb.Error as e:
        print(f"Error while connecting to MariaDB Server:{e}")
        sys.exit(1)

    # Get the cursor
    cur = connect.cursor()

    return (cur, connect)
