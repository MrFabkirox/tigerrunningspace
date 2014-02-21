import sqlite3 as lite
import sys

quotes = (
    (2, 'frog might not be bigger than the cow'),
    (3, 'pink is blue'),
)

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
    cur.execute("CREATE TABLE quotes(strength INTEGER, quote TEXT)")
    cur.executemany("INSERT INTO quotes VALUES(?, ?)", quotes)


with con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS reps")
    cur.execute("CREATE TABLE reps(rep_name TEXT, amount INT)")
    cur.executemany("INSERT INTO reps VALUES(?, ?)", sales)
    
con.close()

