import sqlite3 

import datetime
import decimal

################## Create Tables ######################

def createTables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DROP TABLE IF EXISTS Login"""
    c.execute(q)
    q = """CREATE TABLE IF NOT EXISTS Login (
    Email VARCHAR(255),
    Url TEXT,
    Username VARCHAR(255),
    Password TEXT
    );"""
    c.execute(q)
    q = "DELETE from History"
    c.execute(q)
    conn.close()

createTables()
def addToLogin(email, url, user, pw):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM Login
    WHERE Email=? AND Url=?"""
    c.execute(q, (email, url))
    conn.commit()
    if not c.fetchone():
        print("im lost")
        q = """INSERT INTO Login
        Values (?, ?, ?, ?)"""
        c.execute(q, (email, url, user, pw))
        conn.commit()

    else: 
        print("so we found it")
        q = """UPDATE Login
        SET Username=?, Password=?
        WHERE Email=? And Url=?"""
        c.execute(q, (user, pw, email, url))
        conn.commit()
    conn.commit()
    conn.close()