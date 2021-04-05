import glob

python_list = glob.glob("????.py")
json_list = glob.glob("*.json")
txt_list = glob.glob("*.txt")
subdir_list = glob.glob("**/*.py", recursive=True)
# print(python_list, json_list, txt_list)
# print(subdir_list)


# iterating through every file that ends in .py
for file in glob.iglob('**/[a]*[p]*', recursive=True):
	print(file)

print("finished")