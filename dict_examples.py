dict1 = dict()
print(dict1)
dict2 = {'red': 5, 'white': 18, 'pink': 7, 'green': 9}
print(dict2)
dict3 = {}  # empty dict

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['YCC'])
airports['PIT'] = 'Pittsburgh'
print(airports)
airports['PIT'] = 'Mechanicsburg'
print(airports)

# print(airports['PHL'])
if 'PHL' in airports:
    print(airports['PHL'])

print(airports.get('PHL'))
print(airports.get('PHL'), 100)

print(airports.keys())
print(airports.values())

for abbr, name in airports.items():
    print(abbr, name)
print()


for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

x = airports.setdefault('ALB', 'Albany')
print(x)
print(airports, '\n')