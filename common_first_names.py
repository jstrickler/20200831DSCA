
pm_names = []
with open("DATA/primeministers.txt") as pm_in:
    for line in pm_in:
        fields = line.split(':')
        first_name_parts = fields[1].split()
        if first_name_parts[0] == 'Sir':
            first_name_parts.pop(0)
        first_name = first_name_parts.pop(0)
        pm_names.append(first_name)

potus_names = []
with open("DATA/presidents.txt") as potus_in:
    for line in potus_in:
        fields = line.split(':')
        first_name_parts = fields[2].split()
        first_name = first_name_parts.pop(0)
        potus_names.append(first_name)

pms = set(pm_names)
potus = set(potus_names)

print("common:", pms & potus)  # intersection
print("not common (Xor)", pms ^ potus)   # xor
print("all:", pms | potus)   # union
print("Only POTUS:", potus - pms)
print("Only PMs:", pms - potus)
print()

with open("DATA/breakfast.txt") as breakfast_in:
    foods = (food.rstrip() for food in breakfast_in)
    unique_foods = set(foods)
    print(unique_foods)




