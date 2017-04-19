def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
		
while True:
	while True:	
		user_input = input('How many fibonacci numbers would you like to see?\n')
		if(is_number(user_input)):
			print('\n')
			break
		else:
			print('\nThat is not an integer.')
	i = 0
	First_Value = 0
	Second_Value = 1

	while(i < int(user_input)):
		if(i <= 1):
			Next = i
		else:
			Next = First_Value + Second_Value
			First_Value = Second_Value
			Second_Value = Next
		print(Next)
		i=i+1
		
	cont = input('\nWould you like to enter another number? y/n\n')
	if(cont != 'y'):
		break