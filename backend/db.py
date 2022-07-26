from typing import Dict, List
# environment variables
from dotenv import dotenv_values
# to encode files in base64
import base64
import sqlite3
from sqlite3 import Error

# conn = create_connection('db/assets/stori-newsletter.db')

configEnv = dotenv_values(".env")

def create_connection(db_file):
    
    # :param db_file: database file
    # :return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def setRecipient(conn, recipientData):
    query = "INSERT INTO recipients(name, email) VALUES (?,?)"
    cur = conn.cursor()
    cur.execute(query, recipientData)
    conn.commit()
    return cur.lastrowid

def getRecipients(conn):
    query = 'SELECT * from recipients'
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return cur.fetchall()

def createNewsletter(conn, newsletterData):
    query = "INSERT INTO newsletter(name, content, recipients, asset) VALUES (?,?,?,?)"
    cur = conn.cursor()
    cur.execute(query, newsletterData)
    conn.commit()
    return cur.lastrowid

def getNewsletters(conn):
    query = 'SELECT * from newsletter'
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return cur.fetchall()

def test():
    database = "db/assets/stori-newsletter.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # insertDummy = ('Guillermo', 'memorubioc@gmail.com')
        # setRecipient(conn, insertDummy)
        recipients = getRecipients(conn)
        print(recipients)
# test()