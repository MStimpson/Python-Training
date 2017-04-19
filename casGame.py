from Casino import Dice
from Casino import Cards
import os
#Assigns a number to non-integer values.
def cardPoint(card):
	if(card == 'Ace'):
		return 1
	elif(card == 'King'):
		return 12
	elif(card == 'Queen'):
		return 11
	elif(card == 'Jack'):
		return 10
	else:
		return int(card)
while True:
	#Clears screen - grabs and validates input
	os.system('cls')
	while True:
		user_input = input('Would you like to play blackjack or craps? Enter "blackjack" or "craps"\n')
		if(user_input == 'craps' or user_input == 'blackjack'):
			break
		else:
			print('Not Found.')
	#if user chooses craps.
	if(user_input == 'craps'):
		print('\nIf your first roll is a 7 or 11 you win, 2 or 3 you lose.')
		print('Your subsequent rolls must equal your first roll to win. Rolling a 7 is a loss.')
		print('Rolling two dice now...\n')
		#rolls two die and calculates their sum.
		d = Dice(6)
		rollOne = d.rollDie()
		rollTwo = d.rollDie()
		sum= rollOne + rollTwo
		#Displays sum and check for win/loss
		print('You rolled a ',sum,'\n')
		if(sum == 7 or sum == 11):
			print('You win!\n')
		elif(sum == 2 or sum == 3):
			print('You lose.\n')
		input('Press any key to roll again.\n')
		#If user did not win or lose yet then
		while True:
			secSum = d.rollDie() + d.rollDie()
			print('You rolled a ', secSum, '\n')
			if(sum == secSum):
				print('You win!\n')
				break
			elif(secSum == 7):
				print('You lose.\n')
				break
			input('Press any key to roll again.\n')	
	#If user chooses blackjack
	elif(user_input=='blackjack'):
		#Grabs first two cards from top of deck.
		c = Cards()
		c.shuffleCards()
		pCardOne = cardPoint(c.dealCard())
		pCardTwo = cardPoint(c.dealCard())
		psum = pCardOne + pCardTwo
		###
		if(psum == 21):
			print('You win!\n')
		else:
			dCardOne = cardPoint(c.dealCard())
			dCardTwo = cardPoint(c.dealCard())
			dsum = dCardOne + dCardTwo
			while True:
				#Prints current scores and asks user if they'd like another card.
				print('\nYour score is: ',psum)
				print('The dealers score: ',dsum,'\n')
				if(psum >= 21):
					break
				user_input = input('Would you like another card?y/n\n')
				if(user_input=='y'):
					psum += cardPoint(c.dealCard())
				else:
					break
			#The dealer gets a card if less than 21 and prints scores.
			if(dsum<21):
				print('\nThe dealer gets another card.\n')
				print('Your score is: ',psum)
				dsum += cardPoint(c.dealCard())
				print('The dealers score: ',dsum,'\n')
		#If the player sum and dealer sum is 21 the player wins?			
		if(abs(psum - 21)<=abs(dsum - 21)):
			print('The player wins!\n')
		else:
			print('The dealer wins!\n')
	#Again?			
	user_input = input('Would you like to play another game?y/n\n')
	if(user_input != 'y'):
		break