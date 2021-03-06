# coding=utf-8
import sqlite3


# parameterized queries
# inserts
# selects
# updates
# deletes

# transactions
with sqlite3.connect('data/stocks.db') as conn:
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # Save (commit) the changes
    conn.commit()

    # Select:
    c.execute("SELECT * FROM stocks")
    print(c.fetchone())
