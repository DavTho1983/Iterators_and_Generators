names = ["Eiffel Tower", "Empire State", "Sears Tower", "Burj Khalifa", "Taipei 101"]
heights = [324, 381, 442, 828, 509]
print(list(enumerate(names)))

for num, name in enumerate(names):
    print(num, name)

#zip takes a pair of streams and gives you a stream of pairs
for name, height in zip(names, heights):
    print('%s: %s meters' % (name, height))

skyscrapers = dict(zip(names, heights)) #zips into dict
print(skyscrapers)

print(max(skyscrapers.values())) #gets max value from dict

print(max(skyscrapers.items(), key=lambda b: b[1]))

print(max(skyscrapers, key=skyscrapers.get))
