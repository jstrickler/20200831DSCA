from pprint import pprint

knight_data = {}

file_name = 'DATA/knights.txt'

with open(file_name) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_data[name] = title, color, quest, comment

pprint(knight_data)
print()

for name, fields in knight_data.items():
    print(fields[0], name)
print()

print(knight_data['Lancelot'][2])

