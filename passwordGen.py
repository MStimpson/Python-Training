import random
def strongPass():
	charSet ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
	minLength = 4
	maxLength = 30
	passLength = random.randint(minLength,maxLength)
	password =''
	i=0
	while i < passLength:
		randChar = random.randint(0,len(charSet)-1)
		password += charSet[randChar]
		i+=1
	return password
def weakPass():
	charSet ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	minLength = 4
	maxLength = 30
	passLength = random.randint(minLength,maxLength)
	password =''
	i=0
	while i < passLength:
		randChar = random.randint(0,len(charSet)-1)
		password += charSet[randChar]
		i+=1
	return password
	
while True:
	while True:
		user_input = input('Would you like a weak or strong password?(Type 1 for weak and 2 for strong)\n')
		if(user_input == '1'):
			print(weakPass(), '\n')
			break
		elif(user_input == '2'):
			print(strongPass(),'\n')
			break
		print('That is not valid input.')
	again = input('Would you like to generate another?y/n\n')
	if(again != 'y'):
		break