def is_string(s):
	try:
		float(s)
		return False
	except ValueError:
		return True
#Grab input
while True:
	while True:
		user_input = input('Please enter a word.\n')
		if is_string(user_input): 
			break
		else:
			print('That is not a word\n')
#Process input
#I could also loop through and 
#compare the first index to the last index
	reverse = user_input[::-1]
	if(user_input==reverse):
		print('This word is a palindrome.\n')
	else:
		print('This word is not a palindrome.\n')
#Play again?	
	cont = input('Would you like to enter another word? y/n\n')
	if(cont != 'y'):
		break