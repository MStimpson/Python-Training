from matplotlib import pyplot
import os
script_dir = os.path.dirname(__file__)
rel_path = "data/world_population.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
year=[]
population=[]
for line in file:
	#Learn how to use regex in python
	x=line.replace(' ','#').replace('######','#').replace('#####','#').replace('####','#').replace('###','#').replace('##','#')
	y=x.split('#')
	year.append(y[0])	
	population.append(y[1].replace('\n',''))

pyplot.plot(year,population,'-')
pyplot.ylabel('Population')
pyplot.xlabel('Year')
pyplot.title('World Population Growth')
pyplot.show()