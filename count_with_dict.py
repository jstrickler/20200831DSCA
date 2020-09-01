counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food_item = raw_line.rstrip()

        if food_item not in counts:
            counts[food_item] = 0

        counts[food_item] = counts[food_item] + 1
        # counts[food_item] += 1   SAME


for food, count in counts.items():
    print(food, count)