from matplotlib import pyplot as plt
from matplotlib import style

from numpy import genfromtxt

def liner(filename):
	data = genfromtxt(filename,delimiter=',')

	plt.plot(data)

	plt.title('Info')
	plt.ylabel('Y axis')
	plt.xlabel('X axis')

	plt.show()
	

liner('init.csv')
	
if __name__ == '__main__':
	liner('init.csv')	
