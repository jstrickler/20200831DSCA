import sys
from dsca.misc import dscautils

dscautils.spam()
dscautils.toast()
print()

# DO NOT DO THIS
# dscautils._ham()

for path in sys.path:
    print(path)