import sys

print(sys.argv)    # sys.argv is list of words on the command line

if len(sys.argv) < 5:
    print("Please specify a value on the command line")
    sys.exit(1)

if sys.argv[3].isdigit():
    value = int(sys.argv[3])

print(sys.argv[0])  # script name
print(sys.argv[1])  # first argument that is not the script
print(sys.argv[3])
# print(sys.argv[10])
print(float(sys.argv[4]) * 5)
