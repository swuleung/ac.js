import sqlite3

def add_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """ INSERT OR REPLACE INTO Users 
            VALUES (?)"""
    c.execute(q, (email,))
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

    