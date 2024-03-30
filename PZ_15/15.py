import sqlite3 as sq
from info_i import info_users


with sq.connect('saper.db') as con:
    cur = con.cursor()
    # cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")

# with sq.connect('saper.db') as con:
#     cur = con.cursor()
#     cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)
#     cur.execute("SELECT * FROM users")
#     result = cur.fetchall()
#     print(result)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE score > 1000 ORDER BY score DESC")
    for result in cur:
        print(result)