import sqlite3 

import datetime
import decimal

def add_to_login(email, url, user, pw):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    # q = """SELECT * 
    # FROM Login
    # WHERE EmailIP=? AND Url=?"""
    # c.execute(q, (email, url))
    # conn.commit()
    # if not c.fetchone():
    q = """INSERT OR REPLACE INTO Login
    Values (?, ?, ?, ?, ?)"""
    c.execute(q, (email.replace("\"", ""), url, user, pw, datetime.datetime.now()))
    conn.commit()

    # else:
    #     q = """UPDATE Login
    #     SET Username=?, Password=?, TimeCollected=?
    #     WHERE EmailIP=? And Url=?"""
    #     c.execute(q, (user, pw, datetime.datetime.now(), email.replace("\"", ""), url))
    #     conn.commit()
    # conn.commit()
    conn.close()

def get_logins_by_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM Login
    WHERE EmailIP=?
    ORDER BY Url ASC"""
    data = c.execute(q, (email,)).fetchall()
    conn.commit()
    conn.close()

    return data