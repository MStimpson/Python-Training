import random
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
while True:	
	#Validate and grab input.
	while True:
		user_input = input('Enter number length.\n')
		if(int(user_input) == 0):
			break
		if is_number(user_input):
			break
		print('Not an integer.\n')
	#Generate Secret number.
	i=0
	secret_num=''
	while i<int(user_input):
		secret_num+=str(random.randint(0,9))
		i+=1
	###################
	 print(secret_num)#
	###################
	gameLoop=True
	while True:
		#Validate and grab input.
		while True:
			user_num = input('\nGuess a number!\n\n')
			if(int(len(str(user_num))) != int(user_input)):
				print('Must enter number that is equal length to first number.\n')
			elif(user_num==0): 
				print('Not valid number.\n')
			elif is_number(user_num):
				print('\n')
				break
			else: print('Not an integer.\n')
		#Compare secret number to user number.
		i=0
		cow=0
		for char in secret_num:
			if(char == user_num[i]):
				print('Cow')
				cow+=1
			elif(char in user_num):
				print('Bull')
			if(cow == int(user_input)):
				print('You win!\n')
				gameLoop=False
				break
			i+=1
		if(gameLoop == False):
			break
	#Again
	again = input('Do you want to play again?y/n\n')	
	if(again != 'y'):
			break