import sys
import time
import os

def sortValue(r):
	return result[r]

dir ={"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
		 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
		 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
		 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
		 "x": 8, "z": 10}
result={}
script_dir = os.path.dirname(__file__)
rel_path = "data/sowpods.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
user_input = input('Enter your 7 letters\n')
user_input = user_input.upper()

t0=time.time()

for line in file:
	points = 0
	line = line.strip()
	validWord = True
	us = list(user_input)
	for letter in line:
		if(letter in us):
			us.remove(letter)
			points = points + dir.get(letter.lower())
		else:
			validWord = False
			break
	if(validWord):
		result.update({line:points})

sorted_result = sorted(result, key = sortValue)
for element in sorted_result:
	print(element, '---', result[element])
	
t1= time.time()	
print('\n', t1-t0)
file.close
