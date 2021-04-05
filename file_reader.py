filename = 'pi_digits.txt' 

# accessing lines in a file object
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


# storing lines of a file into a list using .readlines(). these can be accessed outside of a with
with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ""
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

new_file = 'learning_python.txt'

with open(new_file) as new_file_object:
	content = new_file_object.read()
	print(content.replace("Python", "C"))

with open(new_file) as new_file_object:
	for line in new_file_object:
		print(line.rstrip().replace("Python", "C"))

with open(new_file) as new_file_object:
	learnings = new_file_object.readlines()

for line in learnings: 
	print(line.rstrip().replace("Python", "C"))

	