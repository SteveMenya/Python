# sets are collections that dissallow duplicates

s1 = set([1, 2, 3, 2])
print(len(s1))  # prints 3
print(s1.isdisjoint(s1))  # prints False cause the number 2 appears twice

s2 = {4, 5, 6}
print(s1.isdisjoint(s2))  # prints True cause theres no dups betweek s1 and s2

s3 = frozenset([2, 4, 7])
print(s2.difference(s3))  # {5, 6}

records = set()
records.add(('John', 'Smith', 43, 'js@yahoo.com'))
records.add(('Ellen', 'James', 32, 'js@yahoo.com'))
records.add(('Sally', 'Edwards', 36, 'js@yahoo.com'))
records.add(('John', 'Smith', 43, 'js@yahoo.com'))  #This one is not added since its a duplicate

for record in records:
    print(record)
