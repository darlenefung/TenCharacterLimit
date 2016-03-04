# Darlene Fung
#3/2/16

name = raw_input("What is your name? ") # asks the user for input

inputFile = open("input.txt", "w") # creates inputFile
outputFile = open("output.txt", "w")

answer = raw_input("Would you like to add more text to the file? ")
while answer != "no":
	inputFile = open("input.txt", "a")
	lengthAnswer = answer[:10]
	outputFile.write(lengthAnswer + "\n")
	answer = raw_input("Would you like to add more text to the file? ")
	
else: 
	print("{}, check out the output file! (output.txt)".format(name))
	
inputFile.close()
outputFile.close()

	
