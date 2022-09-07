# my list of tuples
records = [
    ('John', 'Smith', 43, 'johns@example.com'),
    ('Steve', 'Smith', 22, 'steves@example.com'),
    ('Menya', 'Smith', 21, 'menyas@example.com'),
    ('Keith', 'Cramer', 12, 'otienos@example.com')
]

# Display Menya Smiths Age
print(records[2][2])

# Add a new record into the records
records.append(('Otieno', 'Smith', 12, 'otienos@example.com'))

# Display how many records you have after this
count = len(records)
print(count)

# Display how many fields are in the record from the end record

count_from_last_two = len(records[-2])
print(count_from_last_two)

# Display how long O Creamers email is
print(len(records[3][3]))

