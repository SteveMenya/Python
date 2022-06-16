print('\nCreating and accessing dicts: ')
my_dict = {}
my_dict = dict()  # or
my_dict = {'pet': 'dog', 'pet2': 'fish'}
my_dict = dict(pet='dog', pet2='fish')  # or

my_dict['pet3'] = 'cat'
print(my_dict)

print('\nIteration dicts: ')
d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
for item in d1:  # Iterating a dictionary returns the keys
    print(item, end=' ')

print('\n\nIterating dict values: ')
for value in d1.values():
    print(value, end=' ')

print('\n\nIterating dict keys and values: ')
for key, value in d1.items():
    print(f'{key} {value}')

print('\nAccessing dicts: ')
print(d1.get('Green'))
print(d1.get('Green', 'No green'))
# print(d1['Green']) #generates error

print('\nSorting with dicts: ')
list3 = sorted(d1.items(), key=lambda item: item[1])
print(list3)

back_to_dict = dict(list3)
print(back_to_dict)