import sqlite3

def create_users_table():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    # q = """DROP TABLE if exists Users"""
    # c.execute(q)
    q = """CREATE TABLE IF NOT EXISTS Users (
    Email VARCHAR(255) UNIQUE);"""
    c.execute(q)
    # q = "DELETE from Users"
    # c.execute(q)
    conn.commit()
    conn.close()

def add_user(email):
    create_users_table()
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

    