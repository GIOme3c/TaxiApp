from mysql.connector import connect, Error
from flask import abort, make_response
from modules import __config


def request_to_db(req_text, change = False):
    try:
        with connect(
            host=__config.host,
            user=__config.user,
            password=__config.password,
            database=__config.database
        ) as connection:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(req_text)
                    if change:
                        try:
                            connection.commit()
                            return True
                        except:
                            connection.rollback()
                            return False
                    else:
                        return cursor.fetchall()
                except Error as e:
                    print("Request Error : ",e)
                    abort(418, description = e)
    except Error as e:
        print("Connection Error : ",e)
        abort(523, description = "Database is down")


def get_connection():
    try:
        with connect(
            host=__config.host,
            user=__config.user,
            password=__config.password,
            database=__config.database
        ) as connection:
            return connection
    except Error as e:
        print("Connection Error : ",e)
        abort(523, description = "Database is down")

def empty_response():
    make_response('',204)