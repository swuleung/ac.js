import sqlite3 

import datetime
import decimal

def addToLogin(email, url, user, pw):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM Login
    WHERE Email=? AND Url=?"""
    c.execute(q, (email, url))
    conn.commit()
    if not c.fetchone():
        q = """INSERT INTO Login
        Values (?, ?, ?, ?)"""
        c.execute(q, (email, url, user, pw))
        conn.commit()

    else:
        q = """UPDATE Login
        SET Username=?, Password=?
        WHERE Email=? And Url=?"""
        c.execute(q, (user, pw, email, url))
        conn.commit()
    conn.commit()
    conn.close()