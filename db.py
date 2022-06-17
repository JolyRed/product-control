import sqlite3


connection = sqlite3.connect('диплом.db')

with connection:
    cur = connection.cursor()
    cur.execute('SELECT * FROM Поставщики')
    rows = cur.fetchall()

    for row in rows:
        print(row)
