bikes = ['trek','cannondale','firestone']
print(bikes[0])
print(bikes[-3])
message = f'I remember the first bike I got in the U.S. It was a red {bikes[-1].title()} and I tore the streets of my neighboerhood in Richmond, VA with it aha'
print(message)

friends = ['abhi', 'javed', 'puneeth', 'varun', 'thomas', 'humayun']

print(f'greetings {friends[0].title()}, {friends[1].title()}, {friends[2].title()}, {friends[3].title()}, {friends[4].title()}, {friends[5].title()}')
# need to figure out how to iterate through each one in a command if possible
# lists are dynamic

# reassigning indicies is standard
bikes[0] = 'test'
bikes.append('ducati')
bikes.insert(0, 'yamaha')
del bikes[0]
popped_bike = bikes.pop(0)
too_expensive = 'ducati'
bikes.remove(too_expensive)
print(bikes)
print(popped_bike)