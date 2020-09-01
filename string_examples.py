"""
This is a script that illustrates string behavior in Python

(c) 2020 John  Strickler
"""
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"

print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')

print("""Guido's the "BDFL" of Python""")

query = """
select *
from recipes
where ingredient = 'parsley'
"""

actor = "Chris Hemsworth"
print(actor)
a1 = actor.upper()
print(a1)
print(actor.upper())

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

print("wo" in actor)
print("bo" in actor)

print(actor.count('h'))
print(actor.count('is'))
print(actor.lower().count('h'))
print(actor.lower().startswith('chris'))

loc = actor.index('worth')
print(loc)
h_count = actor.lower().count('h')
print(h_count)

phrase = "you sold     me a dead\tbird"

words = phrase.split()
print(words)

data = '5,6,7,8'
values = data.split(',')
print(values)

new_data = '/'.join(values)
print(new_data)

s1= "       all my exes live in Texas      "
print("|" + s1.lstrip() + "|")
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")
print()

s2 = "xxxyyyxxyyxyyyyxxxall my exes live in Texasxyxyxyxyxyxyxyxyxyyyyyyyyyyyyyyyyy"
print("|" + s2.lstrip('xy') + "|")
print("|" + s2.rstrip('xy') + "|")
print("|" + s2.strip('xy') + "|")
print()

print(s1.replace(' ', '_'))
print(s1.replace(' ', ''))


print(len(actor), len(s1), len(s2))  # not actor.len()





