import sys
import os

# A simple grep utility

args = sys.argv

if len(args) != 3:
    print('Improper argument provided. Syntax: ')
    print(' python grep.py wordexpression directory')
    sys.exit(42)

wordexpression = args[1]
directory = args[2]
file_list = []

dir_contents = os.listdir(directory)

for entry in dir_contents:
    filename = os.path.join(directory, entry)
    if os.path.isfile(filename):
        file_list.append(filename)

for filename in file_list:
    line_count = 0
    for line in open(filename, encoding='utf-8'):
        line_count += 1
        if line.find(wordexpression) != -1:
            print(f'File: {os.path.basename(filename)}, Line: {line_count}, ({wordexpression})')

my_word = ['my_word/', 'my_word', 'my_word', 'my_word/', 'my_word.', 'my_word', 'my_word', 'my_word', 'my_word', 'my_word', 'my_word']
