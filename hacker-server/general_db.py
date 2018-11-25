import sqlite3

def create_all_tables():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    
    #### Crease Users Table ####
    q = """CREATE TABLE IF NOT EXISTS Users (
    Email VARCHAR(255),
    LastOnline DATETIME,
    PRIMARY KEY (Email)
    );"""
    c.execute(q)

    #### Crease History Table ####
    q = """CREATE TABLE IF NOT EXISTS History (
    Email VARCHAR(255),
    Url TEXT UNIQUE,
    LastVisited DATETIME,
    FOREIGN KEY (Email) REFERENCES Users(Email)
    );"""
    c.execute(q)

    #### Crease Login Table ####
    q = """CREATE TABLE IF NOT EXISTS Login (
    Email VARCHAR(255),
    Url TEXT UNIQUE,
    Username VARCHAR(255),
    Password TEXT,
    TimeCollected DATETIME,
    FOREIGN KEY (Email) REFERENCES Users(Email)
    );"""
    c.execute(q)

    #### Creat Cookies Table ####
    q = """CREATE TABLE IF NOT EXISTS Cookies (
    Email VARCHAR(255),
    Url TEXT,
    CookieKey TEXT,
    CookieVal TEXT,
    TimeCollected DATETIME,
    FOREIGN KEY (Email) REFERENCES Users(Email),
    PRIMARY KEY (Email, Url, CookieKey)
    );"""
    c.execute(q)

    #### Create Secure Table ####
    q = """CREATE TABLE IF NOT EXISTS Secure (
    Email VARCHAR(255),
    Url TEXT,
    FOREIGN KEY (Email) REFERENCES Users(Email)
    );"""
    c.execute(q)

    #### Create Random (?) Table ####
    q = """CREATE TABLE IF NOT EXISTS Random (
    Email VARCHAR(255),
    Url TEXT,
    FOREIGN KEY (Email) REFERENCES Users(Email)
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

    q = "DElETE FROM Users"
    c.execute(q)

    conn.commit()
    conn.close()

    print("All table data have been deleted")
