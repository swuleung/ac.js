import sqlite3
import datetime


def add_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """ INSERT OR REPLACE INTO Users
            VALUES (?, ?)"""
    c.execute(q, (email.replace("\"", ""), datetime.datetime.now()))
    conn.commit()
    conn.close()

def update_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """ UPDATE Users 
            SET LastOnline=?
            WHERE Email=? """
    c.execute(q, (datetime.datetime.now(), email.replace("\"", "")))
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

    