import sqlite3
import datetime


def add_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """ INSERT OR REPLACE INTO Users
            VALUES (?, ?)"""
    c.execute(q, (email.replace("\"", ""), str(datetime.datetime.now())[:-4]))
    conn.commit()
    conn.close()

def update_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """ UPDATE Users 
            SET LastOnline=?
            WHERE EmailIP=? """
    c.execute(q, (str(datetime.datetime.now())[:-4], email.replace("\"", "")))
    conn.commit()
    conn.close()
    
def get_all_users():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """ SELECT * from Users"""
    users=[x[0] for x in c.execute(q).fetchall()]
    conn.commit()
    conn.close()
    return users

def get_online_users(): 
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """ SELECT * FROM Users
            WHERE LastOnline >= datetime('now','localtime','-3 minutes')"""
    data = c.execute(q).fetchall()

    q = """ SELECT datetime('now')"""
    print(c.execute(q).fetchall())
    users = [[str(x[0]), str(x[1])] for x in data]
    conn.close()
    return users