
x = 100   # GLOBAL variable

if x > 50:
    y = "wombat"  # GLOBAL


def spam():
    actor = "Liam Hemsworth"  # LOCAL variable
    print("in spam(): x is", x)
    print("in spam(): y is", y)

    return actor


person = spam()
print("in main: x is", x)
print("in main: y is", y)
print("person is", person)

colors = ['red', 'purple', 'green']


def add_color(color_list):
    color_list.append('pink')


add_color(colors)
print(colors)

animal = "wombat"

def changeit(thing):
    print(thing)
    thing = "wallaby"  # local variable
    print(thing)

changeit(animal)
print(animal)

avg = recalc(avg)

