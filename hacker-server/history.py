import sqlite3 

import datetime
import decimal

################## Create Tables ######################

def createTables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    # q = """DROP TABLE if exists History"""
    # c.execute(q)
    q = """CREATE TABLE IF NOT EXISTS History (
    Email VARCHAR(255),
    Url TEXT UNIQUE,
    LastVisited DATETIME
    );"""
    c.execute(q)
    # q = "DELETE from History"
    # c.execute(q)
    conn.commit()
    conn.close()

createTables()

def addToHistory(email, url, lastvisited):
    createTables()
    s = round(float(lastvisited), 6) / 1000.0
    date = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO History 
            Values (?, ?, ?)"""
    c.execute(q, (email.replace("\"", ""), url, date))
    conn.commit()
    conn.close()

def bulk_add_to_history(email, urls, last_visited):
    createTables()
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    userEmail = email.replace("\"", "")
    for i in range(len(urls)):
        q = """INSERT OR REPLACE INTO History
               Values (?, ?, ?)"""
        s = round(float(last_visited[i]), 6) / 1000.0
        date = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
        c.execute(q, (userEmail, urls[i], date))
    conn.commit()
    conn.close()

def getHistory():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM History"""
    data = c.execute(q).fetchall()
    conn.commit()
    conn.close()

    return data

def get_history_by_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM History
    WHERE Email=?
    ORDER BY LastVisited DESC"""
    data = c.execute(q, (email,)).fetchall()
    conn.commit()
    conn.close()

    return data

