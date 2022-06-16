week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']

# display weekdays
for day in week:
    if day != 'Sun' and day != 'Sat':
        print(day)

records = [
    ('John', 'Smith', 43, 'johns@example.com'),
    ('Ellen', 'James', 22, 'steves@example.com'),
    ('Sally', 'Edward', 21, 'se@example.com'),
    ('Keith', 'Cramer', 12, 'otienos@example.com'),
    ('Brozy', 'T', 29, 'otienos@example.com')
]

# iterating 1
print("*********One**********")
for record in records:
    print(f'{record[0]} {record[1]}, {record[2]} {record[3]}')

# iterating 2
print("*********Two**********")
for record in records:
    print('{0} {1} {2} {3}'.format(*record))

# iterating 3
print("*********Three**********")
for (first, last, age, email) in records:
    print(f'{first} {last} {age} {email}')

for first, last, age, email in records:
    print(f'{first} {last}, {age} {email}'.format(first=first, last=last, age=age, email=email))
