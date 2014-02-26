import sqlite3 as lite
import sys


sales = (
    ('John', 22000),
    ('Dereck', 25000),
    ('zomboy', 35000),
    ('Lily', 20000)
)

con = lite.connect("tiger.db")

with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS quotes")
    cur.execute("CREATE TABLE quotes(quote_id INTEGER PRIMARY KEY AUTOINCREMENT, quote TEXT, status INTEGER)")
    cur.execute("INSERT INTO quotes (quote, status) VALUES('Pink is blue', 1)")


with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS reps")
    cur.execute("CREATE TABLE reps(rep_name TEXT, amount INT)")
    cur.executemany("INSERT INTO reps VALUES(?, ?)", sales)
    
con.close()

