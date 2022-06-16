print("*************Lists*******************")
my_list = []
my_list = list()

my_list = [1, 3, 4]
my_list = [3.3, 'hello', 'hello', 3.3]
my_list = list('hello')

my_list = [5, 2, 3]
print(my_list)
my_list.append(10)
print(my_list)
my_list.insert(4, 'hello')
print(my_list)

print("*************Tuples*******************")
# tuples
my_tuple = ()
my_tuple = tuple()

my_tuple = (1, 3, 5)
print(my_tuple)
my_tuple = (3.3, 'hello', 3.3)
print(my_tuple)
my_tuple = tuple('hello')
print(my_tuple)
my_tuple = (1,)
print(my_tuple)

contact = ('JJ Menya', ['123 Tom Mboya estate', 'Los Angeles', 'CA'])
print(contact[1][0])

print("*************Unpacking*******************")
person = ('Okotcha', 'Esposito', 44, 'test', 'oe@example.com')
first, last, age, t, email = person
print(person[1], last)

first, last, *other = person
print(other)

first, last, age, email, *other = person
print(other)

first, last, *other = person
print(other)