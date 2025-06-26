"""
order should never change
duplicate values are allowed
accept multiple datatypes
growable (insert, delete)
mutable
"""
l=[10,'Hari',True,10+20j,10]
l.append('ram')
print(len(l))
print(l[2])
print(l[0:2])
print(l)