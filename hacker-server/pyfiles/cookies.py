import sqlite3 

import datetime
import decimal
import users

def bulk_add_to_cookies(email, url, cookie):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    userEmail = email.replace("\"", "")
    users.add_user(userEmail)
    cookies = cookie.split("; ")
    for coo in cookies:
        cook = coo.split('=')
        q = """INSERT OR REPLACE INTO Cookies
                Values (?, ?, ?, ?)"""
        c.execute(q, (userEmail, url, cook[0], cook[1]))
        conn.commit()
    conn.close()
    
def get_history_by_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM Cookies
    WHERE Email=?
    ORDER BY Url ASC"""
    data = c.execute(q, (email,)).fetchall()
    conn.commit()
    conn.close()

    return data