import sqlite3 
import datetime
import decimal
from . import users

def bulk_add_to_cookies(email, url, cookie):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    userEmail = email.replace("\"", "")
    users.add_user(userEmail)
    cookies = cookie.split("; ")
    for coo in cookies:
        cook = coo.split('=')
        if (len(cook) >= 2):
            q = """INSERT OR REPLACE INTO Cookies
                    Values (?, ?, ?, ?, ?)"""
            c.execute(q, (userEmail, url, cook[0], '='.join(cook[1:]), datetime.datetime.now()))
            conn.commit()
    conn.close()
    
def get_cookies_by_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM Cookies
    WHERE EmailIP=?
    ORDER BY Url ASC"""
    data = c.execute(q, (email,)).fetchall()
    conn.commit()
    conn.close()

    return data
