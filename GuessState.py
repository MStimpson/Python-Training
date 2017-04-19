#Opens connection to file to be read.
import os
script_dir = os.path.dirname(__file__)
rel_path = "data/States.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
states={}
#Loops through file line by line
for line in file:
	str = line.split(',')
	states.update({str[0]:str[1].replace('\n','')})

#########################
while True:
	i=3
	user_input = input('Enter the name of a state.\n')
	if user_input in states.keys():
		#print(states[user_input])
		while i>0:
			capital=input('What is the states capital?\n')
			if(states[user_input] == capital):
				print('That is correct!')
				break
			else:		
				i=i-1
				print('That is not correct.\n')
				print('You have ', i, ' guesses left.\n')
		print('You are out of gusses!\n')
	else:
		print('I did not find that state.\n')
	cont = input('Would you like to play again? y/n\n')
	if(cont!='y'):
		break
##########################
f.close()
input('Press enter to close')