from glob import glob

for wc in "*.py", "DATA/*.txt", "bugalugs.txt", "*.ipynb", "doit.py":
    result = glob(wc)
    print(result)
    print("=" * 20)

