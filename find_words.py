import re

rx_sep = re.compile(r"[^\w']+")

with open('DATA/parrot.txt') as parrot_in:
    all_text = parrot_in.read()

words = [word.lower() for word in rx_sep.split(all_text)]

unique_words = set(words)

print(words, '\n')
print(unique_words, '\n')

