import dice.Dice
def is_int(n):
	try:
		int(n)
		return True
	except ValueError:
		return False

while True:
	user_input = input('How many sides does the die have?')
	if(is_int):
		break
	else:
		print('You must enter an integer.')

dice = Dice(4)

print(dice.rollDie)