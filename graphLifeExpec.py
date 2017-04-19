from matplotlib import pyplot
from matplotlib import patches
import os
script_dir = os.path.dirname(__file__)
rel_path = "data/life_expectancies_usa.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file = open(abs_file_path, 'r')
year=[]
men=[]
women=[]
for line in file:
	x = line.replace('\n','')
	l = x.split(',')
	year.append(l[0])
	men.append(l[1])
	women.append(l[2])
red_patch = patches.Patch(color='blue',label='Men')
y_patch = patches.Patch(color='orange', label='Women')
pyplot.legend(handles=[red_patch, y_patch])
pyplot.plot(year, men, year, women,'-')
pyplot.ylabel('Age')
pyplot.xlabel('Year')
pyplot.title('Life expectancy')
pyplot.show()