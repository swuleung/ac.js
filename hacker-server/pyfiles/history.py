import sqlite3 

import datetime
import decimal
from . import users

def bulk_add_to_history(email, urls, last_visited):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    userEmail = email.replace("\"", "")
    users.add_user(userEmail)
    for i in range(len(urls)):
        q = """INSERT OR REPLACE INTO History
               Values (?, ?, ?)"""
        s = round(float(last_visited[i]), 6) / 1000.0
        date = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
        c.execute(q, (userEmail, urls[i], date))
    conn.commit()
    conn.close()
    
def get_history_by_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM History
    WHERE EmailIP=?
    ORDER BY LastVisited DESC"""
    data = c.execute(q, (email,)).fetchall()
    conn.commit()
    conn.close()

    return data

