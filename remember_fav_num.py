import json

filename = 'fav_number.json'

with open(filename) as f:
	data = json.load(f)
	print(f"Your favorite number is {data}!")

