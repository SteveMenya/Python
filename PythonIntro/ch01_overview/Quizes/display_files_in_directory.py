"""
This script will prompt for a path and/or pattern to search.
It displays the list of files in order of largest to smallest
"""
import glob
import os

dir_contents = []

path = '..'
match = '*'

for path_item in glob.glob('/'.join([path, match])):
    dir_contents.append(path_item)

print(dir_contents)

files = []

for item in dir_contents:
    if os.path.isfile(item):
        files.append((os.path.basename(item), os.path.getsize(item)))

files.sort(key=lambda file_size: file_size[1], reverse=True)
for name, size in files:
    print(f'{name:<30}{size}')