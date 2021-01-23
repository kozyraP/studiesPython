import sqlite3

conn = sqlite3.connect('wypozyczalnia.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS ksiazki (
                Autor TEXT NOT NULL,
                Tytul TEXT NOT NULL
                );''')

conn.commit()


conn.close()

