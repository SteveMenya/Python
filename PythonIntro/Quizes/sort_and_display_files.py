# Sorts and Displays files in directory

"""
This script will prompt fot a path (and or) pattern to search. It should
display a list of files matching that path in order of largest to smallest
"""

import glob
import os

dir_contents = []

path = '/'
match = '*'

for path_item in glob.glob('/'.join([path, match])):
    dir_contents.append(path_item)

print(dir_contents)

# Solution
# Step1: Iterate over the directory contents to see if they are each files
for item in dir_contents:
    if os.path.isfile(item):
        # Step2:if the item is a file save the filename(not the path) in the file list along with the file size
        file_info = [(os.path.basename(item), os.path.getsize(item))]
        # print(file_info)

        # Step3:Sort the list according to file size
        file_info.sort(key=lambda file_sort: file_sort[1], reverse=True)
        # print(file_info)

for name, size in file_info:
    print(f'{name:}{size}')

files = []
