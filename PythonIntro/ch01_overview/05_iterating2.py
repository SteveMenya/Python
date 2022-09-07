records = [
    ('John', 'Smith', 43, 'johns@example.com'),
    ('Ellen', 'James', 22, 'steves@example.com'),
    ('Sally', 'Edward', 21, 'se@example.com'),
    ('Keith', 'Cramer', 12, 'otienos@example.com'),
    ('Brozy', 'T', 29, 'otienos@example.com')
]
print("*****************Enumerate*********************")
for index, contact in enumerate(records):
    print(index, contact[0])

print("*****************Reversed*********************")
for contact in reversed(records):
    print(contact)

print("*****************EnumerateReversed*********************")
for index, contact in enumerate(reversed(records)):
    print(index, contact[1])

print("*****************Zip*********************")
fruit = ['Apple', 'Orange', 'Banana', 'Watermelon']
color = ['red', 'orange', 'yellow', 'green', 'blue']

for fruit, color in zip(fruit, color):
    print(f'The {fruit} is {color}')
