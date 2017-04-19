from logic import Logic
import sqlite3
import os
import random
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
def game(round):
	
#Initialize
i=0
round=1
playerScore=0
display=''
temp=''
categories=[]
category=''
loop = True
#Includes gameNum in query after done testing.
gameNum = random.randint(1,2000)
#Clear Screen
os.system('cls')
#Connect and grab db information.
connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()
query = 'SELECT clue.text, clue.value, clue.answer, category.name,category.round FROM clue INNER JOIN category ON category.id=clue.category WHERE clue.game=4 AND category.game=4 ORDER BY boardPosition'
cursor.execute(query)
results = cursor.fetchall()
connection.close()	
#Store information in a resultList.
logic = Logic(results)
logic.listResult()
resultList = logic.returnList()
#While loop here

while True:
	loop = True
	resultList = logic.returnList()
	os.system('cls')
	#Grab category if not previously found in list AND in current round.
	display = logic.makeCategories(round)
	categories = logic.showCat(round)
	#Prints avilable categories.
	print(display)
	#Grabs input from user.
	while loop:
		user_input = input('Select a category.\n')
		for item in categories:
			if(user_input.upper() == item):
				category = user_input.upper()
				loop=False
				break
		else:
			print('No match found.\n')
	#Displays a list of values from matching category.
	display=logic.showValue(user_input)
	#Grabs input from user and checks if it's in list. 
	print(display)
	loop=True
	while loop:
		user_input = input('Select a value.\n')		
		for item in resultList:
			if(is_number(user_input)):
				if(int(user_input) == item[1]):
					value = item[1]
					loop=False
					break
		else:
			print('No match.\n')
	#Displays the question and prompts the user for the answer.
	for item in resultList:
		if(item[1]== value and item[3] == category):
			#Currently it prints the answer as well as the question.
			print('\n',item[0],'\n', item[2],'\n')
			user_input = input('Response : ')
			if(item[2].upper() == user_input.upper()):
				print('Correct.')
				playerScore+=value
				#After incrementing player score remove the question from the list.
				#This is used to find the outer index to be removed from the list.
				logic.findIndex(item[0])	
				break
			else:
				#The question is removed even if the answer is incorrect.
				print('Incorrect.')
				playerScore-=value
				logic.findIndex(item[0])
				break
	print('Your new score is $',playerScore,'\n')
	user_input = input('Would you like to try another question?y/n\n')
	if(user_input != 'y'):
		break

#Double jeopardy will start here after I clean up the above code.
#round=1
#final jeopardy will start here after I clean up the above code.
#round=2


