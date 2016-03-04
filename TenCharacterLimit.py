# Darlene Fung
# 3/2/16

name = raw_input("What is your name? ") 															# asks the user for input

inputFile = open("input.txt", "w") 																	# creates input 
outputFile = open("output.txt", "w")																# creates output file 

answer = raw_input("Would you like to add more text to the file? Type 'no' to exit program. ")		# asks the user to enter text, or to exit

while answer != "no":																				# when user is entering information and doesn't want to end the program 
	inputFile = open("input.txt", "a")																# opens input file in append so information can be added
	lengthAnswer = answer[:10]																		# reads first ten characters of the user's answer they typed in
	outputFile.write(lengthAnswer + "\n")															# prints the ten characters in the out put file and adds an enter for the next line of text
	answer = raw_input("Would you like to add more text to the file? Type 'no' to exit program. ")	# asks the user to enter more information, or to exit 
	
else: 
	print("{}, check out the output file! (output.txt)".format(name)) 								# if the user enters "no", it says goodbye
	
inputFile.close()																					# closes input File
outputFile.close()																					# closes output File

	
