# sets are collections that dissallow duplicates

s1 = set([1, 2, 3, 4, 5, 5, 3])
print(len(s1))
print(s1)
"""
prints 
5
{1, 2, 3, 4, 5}
"""

s2 = { 6, 7, 78, 0}
print(s1.isdisjoint(s2))
