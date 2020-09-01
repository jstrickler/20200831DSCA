from itertools import zip_longest
list1 = list()   # new, empty list
cities = ['Scranton', 'Mechanicsburg', 'Carlisle', 'Harrisburg']
list2 = []
all_suits = 'Hearts Diamonds Clubs Spades'
suits = all_suits.split()

print(list1, cities, list2, suits)

cities.append("Shartlesville")

cities.append("Erie")
cities.append("Ohiopyle")

print(cities)

cities.insert(0, 'Hershey')
cities.insert(3, 'Willkes-Barre')
print(cities)

more_cities = ['York', 'Reading', 'Allentown']

cities.extend(more_cities)

print(cities)

del cities[1]  # delete specified element

print(cities)

c = cities.pop()
print(c, cities)

c = cities.pop(4)
print(c, cities)

cities.remove('Erie')
print(cities)

print(cities[0])
print(cities[3])

print(cities[7])
print(cities[-1])
print(cities[len(cities)-1])

#  SLICE    START:STOP:STEP  START:STOP  START: :STOP

print(cities[:3])
print(cities[2:6])
print(cities[-3])
print(cities[-3:])

print(cities[::2])
print()

for city in cities:
    # city = get next element of cities
    print(city.upper())
print()

actor = "Charles Bronson"
for char in actor:
    print(char)
print()

line = "Through all the flimsy things we see at once"

for char in line[1::3]:
    print(char, end=' ')
print('\n')

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for fruit in fruits[1::2]:
    print(fruit)
print()


print(cities)
print(len(cities), min(cities), max(cities),  sorted(cities))
print()

rcities = reversed(cities)
print(rcities, '\n')

for city in rcities:
    print(city)
print()

zz = zip(cities, fruits)

for city, fruit in zz:
    print(city, fruit)
print()

print(list(zip(cities, fruits)))
print(list(zz))

list1 = ['a', 'b', 'c']
list2 = [10, 20, 30]
list3 = ['wombat', 'honey badger', 'pine marten']

for letter, number, animal in zip(list1, list2, list3):
    print(letter, number, animal)
print()

for i, city in enumerate(cities):
    print(i, city)
print()

print(list(enumerate(cities)), '\n')

i = 0
for city in cities:
    print(i, city)
    i += 1
print()

# x = open('file1')
# y = open('file2')
# for f1_value, f2_value in zip(x, y):
#     ....

short_list = ['a', 'b', 'c']

print(list(zip_longest(cities, short_list, fillvalue='WOMBAT')), '\n')


for city in 'Durham', 'Carlisle', 'York', 'Yorktown', 'Reading', 'Writing':
    print(city, city in cities, city not in cities, not city in cities)
print()