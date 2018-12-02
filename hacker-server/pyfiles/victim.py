import sqlite3

def addToVictim(email, script, url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO Victim
    VALUES (?, ?, ?)"""
    c.execute(q, (email, script, url))
    conn.commit()
    conn.close()

def removeFromVictim(email, script, url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DELETE FROM Victim
    WHERE EmailIP=? AND Script=? AND Url=?"""
    c.execute(q, (email, script, url))
    conn.commit()
    conn.close()

def getFromVictim(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT Url 
    FROM Victim
    WHERE EmailIP=?
    """ 
    urls = c.execute(q, (email,)).fetchall()
    conn.close()
    return map(lambda x: str(x[0]), urls)