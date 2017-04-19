import random

def drawCard():
	cardList = [['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace'],['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace'],
				['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace'],['2','3','4','5','6','7','8','9','Jack','Queen','King', 'Ace']]
	str=''			
	selCard = cardList[random.randint(0,3)][random.randint(0,11)]
	i=8
	str+= '----------\n'
	str+='|        |\n'
	str+='|'
	str+=selCard
	while i>(len(selCard)*2):
		str+=' '
		i-=1
	str+='|\n'
	str+='|        |\n'
	str+= '----------\n'
	return str
	
print(drawCard())