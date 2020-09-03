import os

# print(dir(os), '\n')
#
# print(dir(os.path), '\n')

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)

print("file_path:", file_path)

file_size = os.path.getsize(file_path)
print("file size:", file_size)

dir_name = os.path.dirname(file_path)
base_name = os.path.basename(file_path)
print("dir, base:", dir_name, base_name)

abs_path = os.path.abspath(file_path)
print('absolute path:', abs_path)

print(os.access(file_path, os.R_OK | os.W_OK))

for f in 'doit.py', 'didit.py':
    print(os.path.exists(f))
print()

stat_info = os.stat(file_path)
print(stat_info)

print(stat_info.st_uid)

print(os.getlogin())

print(os.getcwd())

old_dir = os.getcwd()

os.chdir('DATA')

print(os.getcwd())

os.chdir(old_dir)

print(os.getcwd())



