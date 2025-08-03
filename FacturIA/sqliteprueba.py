import sqlite3

conn = sqlite3.connect("facturas.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM facturas")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
