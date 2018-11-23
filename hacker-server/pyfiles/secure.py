import sqlite3

def addToSecure(url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO Secure
    VALUES (?)"""
    c.execute(q, (url,))
    conn.commit()
    conn.close()

def addToRandom(url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO Random
    VALUES (?)"""
    c.execute(q, (url,))
    conn.commit()
    conn.close()

def removeFromSecure(url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DELETE FROM Secure
    WHERE url=?"""
    c.execute(q, (url,))
    conn.commit()
    conn.close()

def removeFromRandom(url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DELETE FROM Random
    WHERE url=?"""
    c.execute(q, (url,))
    conn.commit()
    conn.close()

def getFromSecure():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * FROM Secure"""
    urls = c.execute(q).fetchall()
    conn.close()
    return urls

def getFromRandom():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * FROM Random"""
    urls = c.execute(q).fetchall()
    conn.close()
    return urls