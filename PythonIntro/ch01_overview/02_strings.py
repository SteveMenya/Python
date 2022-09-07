# String literal notation

my_string = 'Python\'s great fun'
my_string = "Python's great fun"  # using double "" You dont have to add a breaking \

my_string = """Python's great
fun
"""

"""
    String Random Access and Slicing
"""

my_string = 'Python is great fun'
print(my_string[0])
print(my_string[:9])
print(my_string[0:3])
print(my_string[-9:])

"""String features and Methods"""
# concatenating strings
my_string = 'Python is'
new_string = my_string + " very cool"
print(new_string)

# Split method
my_string = 'Python is great and is the best'
my_list_from_sting = my_string.split(' ')
print(my_list_from_sting)

# Replace method

replace_is_with_is_still = my_string.replace('is', 'is still')
print(replace_is_with_is_still)

# Join method
places = ['The', 'Quick', 'Bird']
join_places_list = ' '.join(places)
print(join_places_list)

# Strip method
new_string = '    Sentence with trailing white spaces at beginning and end     '
print(new_string)
no_white_trail = new_string.strip()
print(no_white_trail)


# find method
my_string = 'Python is great'
word_found = my_string.find('great')
print(word_found)


#using str.format

s = 'It has been raining for {0:.6f} {1} and {0:.4f} {2}'
new_string = s.format(40.001505995055, 'days', 'nights')
print(new_string)

print('{0:10}{1:10}{age:>10}'.format('JJ', 'Menya', age = 4))

name, age = 'Tom', 24
s = f'Hello {name}. Ten year ago, you were \
    {age-10:.1f} years old.'
print(s)




