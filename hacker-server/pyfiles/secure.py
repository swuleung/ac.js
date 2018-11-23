import sqlite3

def addToSecure(email, url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO Secure
    VALUES (?, ?)"""
    c.execute(q, (email, url))
    conn.commit()
    conn.close()

def addToRandom(email, url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO Random
    VALUES (?, ?)"""
    c.execute(q, (email, url))
    conn.commit()
    conn.close()

def removeFromSecure(email, url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DELETE FROM Secure
    WHERE Email=? AND Url=?"""
    c.execute(q, (email, url))
    conn.commit()
    conn.close()

def removeFromRandom(email, url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DELETE FROM Random
    WHERE Email=? AND Url=?"""
    c.execute(q, (email, url))
    conn.commit()
    conn.close()

def getFromSecure(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT Url 
    FROM Secure
    WHERE Email=?
    """ 
    urls = c.execute(q, (email,)).fetchall()
    conn.close()
    return map(lambda x: str(x[0]), urls)

def getFromRandom(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT Url
    FROM Random
    WHERE Email=?
    """
    urls = c.execute(q, (email,)).fetchall()
    conn.close()
    return map(lambda x: str(x[0]), urls)