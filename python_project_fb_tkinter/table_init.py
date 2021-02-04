import sqlite3
import os.path

if os.path.exists('facebook.db'):
    print("DB already exists")
else:
    f = open("facebook.db", "w")
    f.close()
    print("DB created")

conn = sqlite3.connect('facebook.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                name TEXT NOT NULL,
                password TEXT NOT NULL
                );''')

conn.commit()

c.execute('''CREATE TABLE IF NOT EXISTS posts (
                user TEXT NOT NULL,
                post TEXT NOT NULL
                );''')

conn.commit()

c.execute('INSERT INTO users VALUES("Jan","1234");')
c.execute('INSERT INTO users VALUES("Andrzej","1234");')
c.execute('INSERT INTO users VALUES("Pawel","1234");')
conn.commit()

conn.close()
