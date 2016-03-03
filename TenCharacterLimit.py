# Darlene Fung
#3/2/16

inputFile = open("input.txt", "w")
outputFile = open("output.txt", "w")

answer = raw_input("Would you like to add more text to the file? ")
while answer != "no":
	inputFile = open("input.txt", "a")
	lengthAnswer = answer[:10]
	outputFile.write(lengthAnswer + "\n")
	answer = raw_input("Would you like to add more text to the file? ")
	
else: 
	print("Check out the output file! (output.txt)")
	exit()
	
inputFile.close()
outputFile.close()

	
