
praneeth = {
	"height": 6.2,
	"weight_in_lbs": 190,
	"hair_color": 'black'
}

print(praneeth)


# syntax for looping through a dict's k,v pairs
for k,v in praneeth.items():
	print(k, v)

for attribute in praneeth: 
	print(attribute)

for attribute_data in praneeth.values():
	print(attribute_data)