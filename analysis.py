import csv

def analysisCSV():
	first = True
	row = []
	with open('stdlog.csv', 'r') as csvFile:
		reader = csv.reader(csvFile)
		for row in reader:
		    #print(row)		#isinstance(s, str)
		    if(first):
		    	first = False
		    	#print(row)
		    #else:
		    	#print(row)
		    	
	sample_space = int(row[0])
	negative = int(row[1])
	positive = int(row[2])
	no_Detect = sample_space - (positive + negative)
	
	cheating_score = (negative * 100) / sample_space
	
	valid_score = (positive * 100) / sample_space
	
	neutral_score = (no_Detect * 100) / sample_space
		    			
	print("\nResults: cheat probability is = ",cheating_score-5,'\n') #reducing 5% for error
	print("Results: screen time is = ",valid_score,'\n')
	print("Results: NO Detection is =",neutral_score,'\n')
	
	
	if (valid_score <= cheating_score + neutral_score):
		print("Conclusion: HIGH probablility of cheating")
	elif(valid_score >= cheating_score + neutral_score):
		print("Conclusion: LOW probablility of cheating")	
	else:
		print("Conclusion: MEDIUM probablility of cheating")
	
if __name__ == "__main__":
	analysisCSV()
