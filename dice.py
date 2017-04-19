import random
class Dice(object):
	def __init__(self, sides):
		self.sides = sides
	def rollDie(self):
		return random.randint(1,self.sides)
def is_int(n):
	try:
		int(n)
		return True
	except ValueError:
		return False
while True:
	user_input = input('How many sides does the die have?\n')
	if(is_int(user_input)):
		break
	else:
		print('You must enter an integer.\n')

d = Dice(int(user_input))
print(d.rollDie())