
#  int float  bool complex

i1 = 100
i2 = 0b100
i3 = 0x100

print(i1, i2, i3)

x = 802938502938502938520395820359820359820359820395820395820395820935820935802935802938502938502935802983502938502935

print(x * 2)
print()

f1 = 123.456
f2 = 123.
f3 = .456


a = 25
b = 8

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  #  floored division
print(a % b)   # modulus
print(a ** b)  # power

a += 5   # a = a + 5
a /= 10  # a = a / 10
a *= 20
print(a)

# not available
#  a++ a--  ++a --a

value = "125"

x = 25

print(int(value) + x)
print(value + str(x))

# int() float() str() bool() list() dict() set()

d = "DeadBeef"

# print(int(d))

print(int(d, 16))

raw_flags = "100010001"

flags = int(raw_flags, 2)
print(flags)
