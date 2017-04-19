import random
###Dice Class #############################
class Dice(object):
	def __init__(self, sides):
		self.sides = sides
	def rollDie(self):
		return random.randint(1,self.sides)
###Cards Class ###########################
class Cards(object):
	def __init__(self):
		self.cardList = [['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace'],['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace'],
						 ['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace'],['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace']]
	def dealCard(self):
		type = random.randint(0,3)
		if(self.cardList[type][0]):
			str=self.cardList[type].pop(0)
		else:
			#If the list is empty.
			#Refil and call dealCard()
			return 0
		#if(type == 0):
		#	str+=' of Hearts'
		#elif(type == 1):
		#	str+=' of Spades'
		#elif(type == 2):
		#	str+=' of Clubs'
		#else:
		#	str+=' of Diamonds'	
		return str
	def shuffleCards(self):
		random.shuffle(self.cardList[0])
		random.shuffle(self.cardList[1])
		random.shuffle(self.cardList[2])
		random.shuffle(self.cardList[3])
	def showDeck(self):
		return self.cardList
		
