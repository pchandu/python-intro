
# for val in range(1,6):
# 	print(val)

# print(list(range(1,6,2)))

# lets try to print an array of square nums from 1 - 10

# squares = []
# for num in range(1,11):
# 	squares.append(num**2)

# list comprehensions

squares = [value**2 for value in range(1,6)]

print(squares)

# Exercises

# counting to twenty

for num in range(1,21):
	print(num)

one_million = [value for value in range(1,1000001)]
# print(one_million)
print(min(one_million))
print(max(one_million))
print(sum(one_million))

for odd_num in range(1,21,2):
	print(odd_num)

multiples_of_3 = [multiple for multiple in range(3,31,3)]
print(multiples_of_3)

for cube in range(1,11):
	print(cube**3)

cubes = [cube**3 for cube in range(1,11)]
cubes_copy = cubes[:]
cubes_copy.append(11111111)
cubes.append(9999999)
print(cubes_copy)
print(cubes[-3:]) #slicing indicies in a list
print(cubes)