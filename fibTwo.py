#Checks if input is an integer
def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False
#Starts sequence num provided by calcFNum
def fib_num(input,list):
	i=0
	fv = list[0]
	sv = list[1]
	print('Starting at', fv,'\n ')
	print(fv)
	while(i<input):
		if(int(input) <= 1):
			Next = i
		else:
			Next = fv + sv
			fv = sv
			sv = Next
		print(Next)
		i=i+1	
#Rounds input to nearest fnum		
def calcFNum(x):
	i = 0
	prev_value = 0
	First_Value = 0
	Second_Value = 1
	while True:
		if(i <= 1):
			Next = i
		if(x < Next):
			if(abs(x-First_Value)<=abs(x-Second_Value)):
				List=[First_Value, prev_value]
				return List
			else:
				List=[Second_Value, First_Value]
				return List
		else:
			prev_value = First_Value
			Next = First_Value + Second_Value
			First_Value = Second_Value
			Second_Value = Next
		i=i+1
	
#Grab input	
while True:
	while True:	
		user_input = input('How many fibonacci numbers would you like to see?\n')
		if(is_number(user_input)):
			print('\n')
			break
		else:
			print('\nThat is not an integer.')
	while True:
		start = input('Enter where you would like to start.\n')
		if(is_number(start)):
			print('\n')
			break
		else:
			print('\nThat is not an integer.')
#Process input				
	fib_num(int(user_input), calcFNum(int(start)))
#Again?	
	cont = input('\nWould you like to enter another number? y/n\n')
	if(cont != 'y'):
		break