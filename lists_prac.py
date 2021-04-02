# Guest lists

guests = ['elon musk', 'bill gates', 'barack obama', 'sir william osler']
print(guests)

print(f"darn. {guests[-1]} can't make it. we should invite mr. buffet to take his seat.")
del guests[-1]
guests.append('warren buffet')
print(guests)

print(sorted(guests, reverse=True))
print(sorted(guests))
print(guests)
guests.reverse()
print(guests)
guests.reverse()
print(guests)
len(guests)
print(len(guests))