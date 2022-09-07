import glob
import os

print('\nDeleting slices from lists: ')
a = [1, 2, 3, 4, 5]
print(a)
print('\na After Deleting')
del a[1:3]

print(a)    #prints [1, 4, 5]


print('\nBasic list Comprehension: ')
list1 = [1, 2, 3, 4, 5, 6]
print(list1)
list2 = [x*2 for x in list1 if x % 2 == 0]
print(list2)


# revisiting display_files_in_directory using list comprehension
print('\n Refactored display_files_in_directory')

dir_contents = []
path = '.'
match = '*'
for path_items in glob.glob('/'.join([path, match])):
    dir_contents.append(path_items)

files = [(os.path.basename(item), os.path.getsize(item)) for item in dir_contents if os.path.isfile(item)]
files.sort(key=lambda file_info: file_info[1], reverse=True)

for name, size in files:
    print(f'{name:<20}{size}')

print('\nExample using the positional expand operator (*): ')

def avg_temperatures(fri_temp, sat_temp, sun_temp):
    return (fri_temp + sat_temp + sun_temp)/3

temps = [88, 92, 94]
print(avg_temperatures(*temps))