import sqlite3

################## Create Tables ######################
def createTables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    # Secure
    q = """CREATE TABLE IF NOT EXISTS Secure (
        Url TEXT
    );"""
    c.execute(q)
    q = "DELETE FROM Secure"
    c.execute(q)
    # Random
    q = """CREATE TABLE IF NOT EXISTS Random (
        Url TEXT
    );"""
    c.execute(q)
    q = "DELETE FROM Random"
    c.execute(q)
    conn.close()

createTables()

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