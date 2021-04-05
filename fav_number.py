import json

filename = 'fav_number.json'

try:
	with open(filename) as f:
		data = json.load(f)
		print(f"Your favorite number is {data}!")
except FileNotFoundError:
	fav_number = input("What is your favorite number? ")

	with open(filename, 'w') as f:
		json.dump(fav_number, f)
