import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute('SELECT name FROM category LIMIT 10')
results = cursor.fetchall()

print(results)
connection.close()