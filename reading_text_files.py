
mary_in = open('DATA/mary.txt')
mary_in.close()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:   # mary_in.readline()
        # print(repr(raw_line))
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("COOKED:")
    print(contents)
print('-' * 60)

with open('DATA/fruit1.txt', 'r') as fruit1_in:
    fruits1 = (f.rstrip() for f in fruit1_in)
    with open('DATA/fruit2.txt', 'r') as fruit2_in:
        fruits2 = (f.rstrip() for f in fruit2_in)
        fruit_pairs = zip(fruits1, fruits2)

        with open('fruit_pairs.txt', 'w') as fruit_pairs_out:
            for f1, f2, in fruit_pairs:
                fruit_pairs_out.write(f"{f1}\t{f2}\n")
print()

# modes (add b for binary)
#  r -- read
#  w -- write
#  a -- append
#  x -- exclusive


print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
print(all_lines)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = [line.rstrip() for line in mary_in]
print(all_lines)
