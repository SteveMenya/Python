from datetime import datetime

x = 10
print(x)
print(type(x))

x = 'hello'
print(x)
print(type(x))

# some PEP 8 Conventions

say_hello = 'hi'


def my_func():
    print(say_hello)


my_func()


class SomeFunClass(object):
    pass


def my_func2(arg1, arg2, arg3, arg4, arg5, arg6): pass


days = [1, 2, 3]

today = datetime.now()

if today.isoweekday() == 5:
    print('TGIF')
print(today)

# Strings Random Accees and Slicing

my_str = 'Python is fun '
for l in my_str:
    print(l)
print(my_str[0])
print(my_str[-13])
print(my_str[2])

# String methods

# split
my_str2 = str('Python is great')
my_list_split = my_str2.split(' ')

# replace
my_list_replace = my_str2.replace('is', 'is still')
print(my_str2)
print(my_list_split)
print(my_list_replace)

# join
print(' '.join(my_list_split))

# strip
new_str = str('         My string with spaces at beginning and end            ')
print(new_str)
print(new_str.strip())

# sequence Unpacking in Python allows for individual variables to be assigned to field in sequence

# Control Structures
print('***************Control Structures********************')

# Using the for loop

week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for day in week:
    if day != 'Sun' and day != 'Sat':
        print('Weekday: ' + day)

# Using string.format

s = 'It has been raining for {0:.2f} {1} and {0:.4f} {2}'
new_string = s.format(40.001, 'days', 'nights')
print(new_string)

# format() with Keywords string

s = '{0} is over {age: 0.2f} {time} old.'.format('Python', time='years', age=25)
print(s)

# f-strings (Formatting Strings)
name, age, time = 'JJ', 42, 'years'

s = f'{name} was {age - 15:.1f} {time} a decade ago'
print(s)

# removing suffix
suffix_string = 'The quick brown fox'
print(suffix_string.removesuffix('fox'))
