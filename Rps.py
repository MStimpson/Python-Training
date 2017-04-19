#Grab input
while True:
	while True:
		p1_input = input('Player 1 enter rock, paper, or scissors.\n')
		if p1_input == 'rock' or p1_input == 'paper' or p1_input == 'scissors':
			break
		else:
			print('That is not valid input.\n')
	while True:		
		p2_input = input('Player 2 enter rock, paper, or scissors.\n')
		if p2_input == 'rock' or p2_input == 'paper' or p2_input == 'scissors':
			break
		else:
			print('That is not valid input.\n\n')
#Process input			
	if p1_input == 'rock':
		if p2_input == 'rock':
			print('It is a draw!')
		if p2_input == 'paper':
			print('Player 2 wins!')
		if p2_input == 'scissors':
			print('Player 1 wins!')
	elif p1_input == 'paper':
		if p2_input == 'rock':
			print('Player 1 wins!')
		if p2_input == 'paper':
			print('It is a draw!')
		if p2_input == 'scissors':
			print('Player 2 wins!')
	elif p1_input == 'scissors':
		if p2_input == 'rock':
			print('Player 2 wins!')
		if p2_input == 'paper':
			print('Player 1 wins!')
		if p2_input == 'scissors':
			print('It is a draw!')
#Play again?
	cont = input('Would you like to play again? y/n\n')
	if cont != 'y':
		break