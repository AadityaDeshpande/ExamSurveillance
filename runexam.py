import cv2
import multiprocessing
from multiprocessing import Process
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import csv

#from graph import bargraph
import sys
from logger import log,initlogger
from line import liner
from analysis import analysisCSV


def exam():
	cap = cv2.VideoCapture(0)
	faces,eyes = [],[]
	
	frame_no = 0
	look_screen = 0
	look_away = 0

	# Create the haar cascade
	
	faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	
	eyesCascade = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
	
	
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		
		frame_no = frame_no + 1
		
		glob[0] = frame_no 
		
		#print("Current Frame number is: ",frame_no)
		
		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.25,	#1.25 1.1 perfect-> 1.25
			minNeighbors=9,  	#5  9-> only single face 
			minSize=(30, 30) 	#30 30 
								#flags = cv2.CV_HAAR_SCALE_IMAGE
		)
		for (x, y, w, h) in faces:
		
			cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
			
			#croping face and finding eyes only in that region
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = frame[y:y+h, x:x+w]
			
			
			eyes = eyesCascade.detectMultiScale(
				gray,
				scaleFactor=1.22, 	# perfect -> 1.2 |1.3 1.1 
				minNeighbors=7,		#perfect->4 5
				minSize=(30, 30) 	#30 30 
									#flags = cv2.CV_HAAR_SCALE_IMAGE)
				)
				
			for (ex, ey, ew, eh) in eyes:
				cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (138,43,226), 2)
		
		#if len(faces) >= 1:
		if len(eyes) == 2:
			print("STATUS ",frame_no," : person LOOKING at SCREEN")
			look_screen = look_screen+1
			glob[2] = look_screen	
		elif len(eyes) == 0:
			print("STATUS ",frame_no," : NO EYES DETECTED")
		elif len(eyes) == 1:
			print("STATUS ",frame_no," : person LOOKING AWAY")
			look_away = look_away+1
			glob[1] = look_away
		
		
		
		#frame = cv2.resize(frame, (600,600))
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):  #if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()






def p2():	#Creating a Log files about student analysis	
	'''with open('logfile1.csv','w',newline='') as csvfile:
		fieldnames = ['frame_number', 'look_away', 'look_screen']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		while True:
			writer.writerow({'frame_number': int(glob[0]), 'look_away': int(glob[1]), 'look_screen': int(glob[2])})
			time.sleep()
	'''
	while True:
		log(glob[0],glob[1],glob[2])
		time.sleep(0.05)


if __name__ == '__main__':
	#exam()
	glob = multiprocessing.Array('i', 4)
	# 0th location contains frame_no 1st-> look_away 2nd -> look_screen
	
	exam = Process(target = exam)
	p2 = Process(target = p2)
	
	print("prepairing....")
	sys.stdout.flush()
	time.sleep(1)
	
	exam.start()
	time.sleep(2)
	
	initlogger()
	
	#print("started") 2nd process goes here
	p2.start()
	
	exam.join()
	
	if not(exam.is_alive()):
		#print("Time to terminate process 2")
		p2.terminate()
		#bargraph(glob[0],glob[1],glob[2])
	#p2.join()
	
	print("\nBlue line = frame number\nGreen line = number of time screen look")
	print("Orange line = number of time away look")
	analysisCSV()
	liner('stdlog.csv')
	#for drawing bar graph
	
	#print("Analysing Data....")
	#sys.stdout.flush()
	#time.sleep(1)
	#bargraph(glob[0],glob[1],glob[2])
	
	
	
	
	
	
	
