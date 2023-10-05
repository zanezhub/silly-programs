import sqlite3
conn = sqlite3.connect("db/db.sqlite")
c = conn.cursor()
c.execute("SELECT title, cat, size, hash FROM items")

for row in c.fetchall():
    try:
        gb = row[2]/(1024 * 1024 * 1024)
        print(f"{row[0]}, {row[1]}, {gb:.2f}GB, {row[3]}")
    except:
        continue