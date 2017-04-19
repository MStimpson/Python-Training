from logic import Logic
from pygame import mixer
import sqlite3
import os
import sys
import random
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
def game(round,p):
	#Initialize
	playerScore=p
	display=''
	temp=''
	categories=[]
	category=''

	while True:
		loop = True
		resultList = logic.returnList()
		os.system('cls')
		if(round==1):
			print('Round 2 is starting now!\n')
		elif(round==2):
			print('The final round is starting!\n')
		#Grab category if not previously found in list AND in current round.
		display = logic.makeCategories(round)
		categories = logic.showCat(round)
		#Prints avilable categories.
		print(display)
		#Grabs input from user.
		while loop:
			if(round==2):
				for item in categories:
					user_input = item
					break
			else:
				user_input = input('Select a category.\n')
			#lets break from loop at any time.
			if(user_input=='`'):
				sys.exit()
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
		if(round != 2):
			print(display)
		loop=True
		while loop:
			if(round==2):
				user_input = 0
			else:
				user_input = input('Select a value.\n')
			#lets break from loop at any time.
			if(user_input=='`'):
				sys.exit()			
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
				if(round == 2):
					input('Press any key when ready!')
					#Plays jeopardy sound on the last question.
					#It would be cool to force the user to answer the question in the length of the song.
					mixer.init()
					mixer.music.load('timer.mp3')
					mixer.music.play()
				print('\n',item[0],'\n', item[2],'\n')
				user_input = input('Response : ')
				if(round == 2):
					mixer.music.stop()
				#lets break from loop at any time.
				if(user_input=='`'):
					sys.exit()
				if(item[2].upper() == user_input.upper()):
					print('Correct.')
					if(round==2):
						playerScore=playerScore*2
					else:
						playerScore+=value
					#After incrementing player score remove the question from the list.
					#This is used to find the outer index to be removed from the list.
					logic.findIndex(item[0])	
					break
				else:
					#The question is removed even if the answer is incorrect.
					print('Incorrect.')
					if(round==2):
						if(playerScore != 0):
							playerScore=playerScore/2
					else:
						playerScore-=value
					logic.findIndex(item[0])
					break
		if(round == 2):
			print('Your final score is $',playerScore,'\n')
			print('Thanks for playing!')
			return playerScore
		else:
			print('Your new score is $',playerScore,'\n')
		user_input = input('Would you like to try another question?y/n\n')
		if(user_input != 'y'):
			return playerScore
#Includes gameNum in query after done testing.
playerScore=0
gameNum = random.randint(1,2000)
#Clear Screen
os.system('cls')
#Connect and grab db information.
connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()
query = 'SELECT clue.text, clue.value, clue.answer, category.name,category.round FROM clue INNER JOIN category ON category.id=clue.category WHERE clue.game='+str(gameNum)+' AND category.game='+str(gameNum)+' ORDER BY boardPosition'
cursor.execute(query)
results = cursor.fetchall()
connection.close()
if(not all(results)):
	print('There was an error.')
	sys.exit()
#Store information in a resultList.
logic = Logic(results)
logic.listResult()
resultList = logic.returnList()
#game
round=0
playerScore=game(round,playerScore)
round=1
playerScore=game(round,playerScore)
round=2
playerScore=game(round,playerScore)
#Round 2 only has one question and it's value is 0?