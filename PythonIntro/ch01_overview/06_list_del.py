data =None
a = [1, 'foo', (), 3.3, str(data), data]
print(a)

# remove 2nd item
del a[1]
print(a)

#remove first and second item after last removal
del a[0:2]
print(a)