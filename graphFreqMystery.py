import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy
import matplotlib.pyplot as plt
import os
script_dir = os.path.dirname(__file__)
rel_path = "data/mystery.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')

dir ={	"a": 0, "c": 0, "b": 0, "e": 0, "d": 0, "g": 0,
		"f": 0, "i": 0, "h": 0, "k": 0, "j": 0, "m": 0,
		"l": 0, "o": 0, "n": 0, "q": 0, "p": 0, "s": 0,
		"r": 0, "u": 0, "t": 0, "w": 0, "v": 0, "y": 0,
		"x": 0, "z": 0}
		
for line in file:
	i=0
	while i<len(line):
		if(line[i] in dir.keys()):
			dir[line[i]]+=1
		i+=1

y_pos =	numpy.arange(len(dir))
		
plt.bar(y_pos, dir.values(), align='center', alpha=0.5)
plt.xticks(y_pos, dir.keys())
plt.ylabel('Frequency')
plt.title('Frequency of letters')
plt.show()