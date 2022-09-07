from collections import namedtuple

Contact = namedtuple('Contact', 'first last age email')

records = [
    Contact('John', 'Collins', 43, 'johns@example.com'),
    Contact('Steve', 'Bakari', 22, 'steves@example.com'),
    Contact('Menya', 'Smith', 21, 'menyas@example.com'),
    Contact('Keith', 'Cramer', 12, 'otienos@example.com')
]

records.sort(key=lambda one_rec: one_rec.age, reverse=True)

for record in records:
    print(record.last, record.age)