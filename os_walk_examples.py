import os

START_DIR = "."

for folder, subfolders, files in os.walk(START_DIR):
    if '.git' in subfolders:
        subfolders.remove('.git')
    print(folder)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            if file_size > 1000:
                print(f"    {file_size:4d} {file_name}")
