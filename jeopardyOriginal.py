import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute('SELECT text, answer, value FROM clue LIMIT 5')
results = cursor.fetchall()

clue =[]
i=0
for items in results:
	x=0
	l=[]
	for item in results[i]:
		l.append(results[i][x])
		x+=1
	clue.append(l)
	i+=1	
print('[$',clue[0][2],']')

connection.close()