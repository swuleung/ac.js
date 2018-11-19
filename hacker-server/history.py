import sqlite3 

import datetime
import decimal

################## Create Tables ######################

def createTables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DROP TABLE if exists History"""
    c.execute(q)
    q = """CREATE TABLE IF NOT EXISTS History (
    Email VARCHAR(255),
    Url TEXT,
    LastVisited DATETIME
    );"""
    c.execute(q)
    q = "DELETE from History"
    c.execute(q)
    conn.close()
createTables()
def addToHistory(email, url, lastvisited):
    # createTables()
    s = round(float(lastvisited), 0) / 1000.0
    datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO History
    Values (?, ?, ?)"""
    c.execute(q, (email, url, lastvisited))
    conn.commit()
    conn.close()