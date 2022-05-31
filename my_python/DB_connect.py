
import mariadb
import sys

# connect to the DB : return the connection and the cursor
def connection():
    try:
        connect = mariadb.connect(
            user = "username",
            password = "password",
            database= "DB name"
        )
    except mariadb.Error as e:
        print(f"Error while connecting to MariaDB Server:{e}")
        sys.exit(1)

    # Get the cursor
    cur = connect.cursor()

    return (cur, connect)
