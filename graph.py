#this file is only used for display bar graph

import matplotlib.pyplot as plt
import numpy as np
import time

def bargraph(a,b,c):
	glob = [a,b,c]
	objects = ('fps', 'away', 'screen')
	y_pos = np.arange(len(objects))
	performance = [glob[0],glob[1],glob[2]]

	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('total')
	plt.title('student analysis')

	plt.show()
	
	#time.sleep(5)
	#plt.close()

bargraph(0,0,0)	
#if __name__ == '__main__':
#	bargraph(0,0,0)


