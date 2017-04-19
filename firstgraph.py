from matplotlib import pyplot
import random

user_input = input('Enter num of x:\n')
l=[]
i=0
while i < int(user_input):
	l.append(random.randint(0,10))
	i = i+1

pyplot.plot(l,'-o')
pyplot.ylabel('Values')
pyplot.xlabel('Time')
pyplot.title('Test Graph')
pyplot.show()