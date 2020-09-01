

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person[0], person[1])
print(len(person))

print(person[:2])

first_name, last_name, product, dob = person    # unpack an iterable to a list of variables

print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

print(type(people))
print(type(people[0]), people[0])
print(type(people[0][0]), people[0][0])
print()

for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = <next-element-of-people>

    print("{}, {} {} ({})".format(last_name, first_name, dob, product))
print()


values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon', 'eta']

a, b, *c = values
print(a, b, c)

a, *b, c = values
print(a, b, c)

*a, b, c = values
print(a, b, c)






