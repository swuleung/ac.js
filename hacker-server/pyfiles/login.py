import sqlite3 

import datetime
import decimal

def add_to_login(email, url, user, pw):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT OR REPLACE INTO Login
    Values (?, ?, ?, ?, ?)"""
    c.execute(q, (email.replace("\"", ""), url, user, pw, datetime.datetime.now()))
    conn.commit()
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

def get_login_kw():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT *
    FROM LoginKW""" 
    data = c.execute(q).fetchall()
    conn.close()
    return [str(x[0]) for x in data]

def add_login_kw(word):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO LoginKW VALUES(?)"""
    c.execute(q,(word,))
    conn.commit()
    conn.close()

def delete_login_kw(word):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DELETE FROM LoginKW 
    WHERE KeyWord=?"""
    c.execute(q,(word,))
    conn.commit()
    conn.close()
