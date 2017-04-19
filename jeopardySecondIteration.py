import sqlite3
import os
os.system('cls')
connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute('SELECT clue.text, clue.value, clue.answer, category.name,category.round FROM clue INNER JOIN category ON category.id=clue.category WHERE clue.game=4 AND category.game=4 AND round=0 ORDER BY boardPosition')
results = cursor.fetchall()
#Pulls information for categories
print(results)
category =[]
i=0
for items in results:
	x=0
	l=[]
	for item in results[i]:
		l.append(results[i][x])
		x+=1
	category.append(l)
	i+=1
	
#creates display
round=0
header=''
for item in category:
	if(item[1] == round):
		i=20
		header+='**********************\n'
		header+='*'
		header+=item[0]
		while i>len(item[0]):
			header+=' '
			i-=1
		header+='*\n'
		header+='**********************\n'		
print(header)
sys.exit()
######
loop=True
while loop:
	user_input = input('Which category would you like to select from?\n')
	for item in category:
		if(item[1]==round):
			if(user_input.upper() == item[0]):
			#print out questions in category
				id=item[2]
				loop=False
				break		
	else:
		print('Nothing found.\n')
if(loop==False):
	query = 'SELECT value FROM clue WHERE game = 4 AND category = '+str (id)
	cursor.execute(query)
	results = cursor.fetchall()
	print(results)
connection.close()	