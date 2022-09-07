# Example1 in-place sort
print('Basic sort: ')
items = [37, 2, 0, -14]
print(items)
items.sort()
print(items)  # prints [-14, 0, 2, 37]

# creating a new list by sorting
items = [37, 2, 0, -14]
new_items = sorted(items)
print(new_items)  # prints [-14, 0, 2, 37]

# sorting in reverse(both in-place and returning a new list)
print('\nUsing reverse=True: ')
items = [37, 2, 0, -14]
items.sort(reverse=True)
print(items)

items = [37, 2, 0, -14]
new_items = sorted(items, reverse=True)
print(items, new_items)

# not the unexpected sort results
print('\nUnexpected sort results: ')
nums = ['13', '1', '11', '4']
nums.sort()
print(nums)  # Prints: ['1', '11', '13', '4'] because sees these as strings and not ints

print('\nUsing keys= ')


# sort using a key
def sort_func(val):
    return int(val)


nums.sort(key=sort_func)
print(nums)  # prints ['1', '4', '11', '13']


# sorted() using a key
def sort_func(val):
    return int(val)


nums2 = sorted(nums, key=sort_func)
print(nums2)

# lambda examples
print('\nExamples with lambdas: ')
calc_square = lambda val: val * val
print(calc_square(10))

# sorting records using a key and labda
records = [
    ('John', 'Smith', 43, 'johns@example.com'),
    ('Ellen', 'James', 22, 'steves@example.com'),
    ('Sally', 'Edward', 21, 'se@example.com'),
    ('Keith', 'Cramer', 12, 'otienos@example.com'),
    ('Brozy', 'T', 29, 'otienos@example.com')
]

records.sort(key=lambda one_rec: one_rec[2], reverse=True)
for record in records:
    print(record)
