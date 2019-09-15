import time
import csv
#need to write init for file creation
'''
def log(a,b,c):
	
	with open(r'stdlog.csv', 'ab', newline='') as csvfile:
		fieldnames = ['frame_number', 'look_away', 'look_screen']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writerow({'frame_number': int(a), 'look_away': int(b), 'look_screen': int(c)})
'''
'''
def log(a,b,c):
	with open('stdlog.csv','a') as fd:
		mystr = str(a)+","+str(b)+","+str(c)
		print(mystr)
		fd.write(str(mystr))

'''
def log(a,b,c):
#	f = open('foo.csv', 'wb')
	with open('stdlog.csv', 'a') as newFile:
		newFileWriter = csv.writer(newFile)
		newFileWriter.writerow([a,b,c])
		#newFileWriter.writerow([4, 'yyy'])
		#newFileWriter.writerow([5, 'zzz'])

def initlogger():
	with open('stdlog.csv','w') as newFile:
		newFileWriter = csv.writer(newFile)
		newFileWriter.writerow(['frame_number', 'look_away', 'look_screen'])

if __name__ == '__main__':
	initlogger()
	log(1,1,1)		
