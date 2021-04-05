filename = 'test.txt'

with open(filename, 'w') as file_obj:
	file_obj.write("wow. we can write into files directly from a py program!\n")
	file_obj.write("don't forget though, python can only read and write strings.\n")
	file_obj.write("if we want to store numerical data, convert it to a string first via str()\n")

with open(filename, 'a') as file_obj:
	file_obj.write("Not everything has to be destroyed with append mode.\n")


new_file = "new_file.txt"

with open(new_file, 'w') as new_file_obj:
	userInput = input("What text would you like to add to the new file?")
	while (userInput != "quit"): 
		userInput = input("What text would you like to add to the new file? ")
		userInput += "\n"
		new_file_obj.write(userInput)