

file_name = "mumbo_jumbo.txt"

try:
    with open(file_name) as file_in:
        for line in file_in:
            print(line.rstrip())
except FileNotFoundError as err:
    print(err)



with open('DATA/breakfast.txt') as breakfast_in:
    foods = [line.rstrip() for line in breakfast_in]
print(len(foods))

try:
    print(foods[99])
except IndexError as err:
    print(err)

values = 5.6, 8.9, 0.0, 6.4, "1.8", 7.1

for v in values:
    try:
        result = 13 / v
    except ZeroDivisionError as wombat:
        print(wombat, type(wombat))
    except (TypeError, ValueError) as err:
        print(err)
        exit(1)
    except Exception as err:
        print("UNEXPECTED!", err)
    else:
        print(result)
    finally:
        print("FINALLY!")

print("All done.")

import sqlite3

try:
    wombat_conn = None
    wombat_conn = sqlite3.connect("wombat.db")
except sqlite3.DatabaseError as err:
    print(err)
else:
    # work with connection ....
finally:
    if wombat_conn:
        wombat_conn.close()