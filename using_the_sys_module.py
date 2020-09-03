import sys

print(sys.argv, '\n')

for path in sys.path:
    print(path)
print()

print(sys.prefix)
print(sys.executable)
print()

print(sys.version)
print(sys.version_info)
print(sys.version_info.major, sys.version_info.minor)
print()

print(sys.platform, '\n')

print(sys.modules.keys(), '\n')

import re

x = sys.modules['re'].compile(r'foo')
print(x)

print(sys.modules['re'], '\n')

# dir()

print(dir(sys), '\n')

print(f"{sys.maxsize:,d}\n")

x = 23948209348203948203948203948203948203948203948203948209348203948209348029348029348029348029348029384029384029384029834029834029834029834029834029834029834029843029834092834820482039482093480293840293840298340928340982304982093482093840293840293840982

print(x)

# sys.stdin  sys.stdout  sys.stderr

print("We have a problem", file=sys.stderr)

with open("delete_me.txt", "w") as delete_me_out:
    for fruit in 'apple', 'banana', 'raspberry':
        print(fruit, file=delete_me_out)










