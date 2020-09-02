from operator import itemgetter

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1:", n1, '\n')

n2 = sorted(nums, reverse=True)
print("n2:", n2, '\n')

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

x = "WINGNUT"

print(x.lower())
print(str.lower(x))
print()

f2 = sorted(fruits, key=str.lower)
print("f2:", f2, '\n')

def ignore_case(s):
    return s.lower()


f3 = sorted(fruits, key=ignore_case)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')


def custom1(fruit):
    return len(fruit), fruit.lower()


f5 = sorted(fruits, key=custom1)
print("f5:", f5, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print()


def by_dob(person):
    return person[-1]


for person in sorted(people, key=by_dob):
    print(person)


def fname_lname(person):
    return person[1], person[0]

for person in sorted(people, key=fname_lname):
    print(person)
print()


def field_getter(field_index):  # function factory -- it makes functions

    def temp(record):
        return record[field_index]

    return temp


for person in sorted(people, key=field_getter(2)):
    print(person)
print()

for person in sorted(people, key=itemgetter(1, 0)):
    print(person)
print()

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

for code, name in sorted(airports.items()):
    print(code, name)
print()

print(airports.items(), '\n')


def by_value(element):  # sort ANY dictionary by value, then key  (default is key then value)
    return element[1], element[0]


for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print()


for code, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(code, name)
print()

# lambda param ... : return-value


for code, name in sorted(airports.items(), key=lambda e: (e[1], e[0]), reverse=True):  # descending sort
    print(code, name)
print()


print(fruits, '\n')
fruits.sort(key=str.lower)
print(fruits, '\n')

#  lambda param: something

