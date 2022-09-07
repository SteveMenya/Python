# list comprehension

list1 = [1, 2, 3, 4, 5]
list2 = [x * 2 for x in list1]
print(list2)

list3 = [x * 2 for x in list1 if x % 2 == 0]
print(list3)