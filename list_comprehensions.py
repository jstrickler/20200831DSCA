fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]  # list comprehension
print("f1:", f1, '\n')

#  [ EXPR for VAR ... in ITERABLE if CONDITION ... ]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

words = ['spam\n', 'ham\n', 'eggs\n']
trimmed_words = [w.rstrip() for w in words]
print("trimmed_words:", trimmed_words, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

numbers = [5.8, 6.3, 4.7, 1.9, 8.8, 8.3, 2.2]
n1 = [int(i) for i in numbers]
print("n1:", n1, '\n')

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

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

f4 = [len(f) for f in fruits]
print("f4:", f4, '\n')


fgen1 = (f.upper() for f in fruits)  # generator expression
print(fgen1)
for fruit in fgen1:
    print(fruit, end=' ')
print('\n')



