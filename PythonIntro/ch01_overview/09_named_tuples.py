from collections import namedtuple

Contact = namedtuple('Contact', 'first last age email')

records = [
    Contact('John', 'Smith', 43, 'johns@example.com'),
    Contact('Ellen', 'James', 22, 'steves@example.com'),
    Contact('Sally', 'Edward', 21, 'se@example.com'),
    Contact('Keith', 'Cramer', 12, 'otienos@example.com'),
    Contact('Brozy', 'T', 29, 'otienos@example.com')
]

records.sort(key=lambda one_rec: one_rec.age, reverse=True)

for record in records:
    print(record.last, record.age)