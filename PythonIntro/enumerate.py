records = [
    ('John', 'Otieno', 43, 'johns@example.com'),
    ('Steve', 'Janyoyo', 22, 'steves@example.com'),
    ('Menya', 'Smith', 21, 'menyas@example.com'),
    ('Keith', 'Cramer', 12, 'otienos@example.com')
]

for index, contact in enumerate(records):
    print(index, contact[1])

print('**********Reverse*************')
for contact in reversed(records):
    print(contact[1])
