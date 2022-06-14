# dictionaries are collections of name/value pairs

my_dict = {}

d1 = {'Smith': 43, 'James': 32, 'Edwards': 36, 'Cramer': 29}
print(d1['Smith'])

J = d1.get('JJ')
print(J)

# looping over a dictionary
# returns keys
for item in d1:
    print(item)

# returns values
for item in d1.values():
    print(item)

# returns keys and values
for key, val in d1.items():
    print(f'{key} comma{val}')
