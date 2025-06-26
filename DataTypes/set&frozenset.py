"""
unordered
mutable
no index values
not allow duplicate values
no slicing
growable
"""
s1={10,'Hari',True,10+20j,10}
s1.add('ram')
print(len(s1))
#print(s[2])
print(s1)
print("-------------------------------")
#Frozenset
"""
same as set only difference is it is immutable
"""
s={10,'Hari',True,10+20j,10}
fs=frozenset(s)
print(type(fs))
#immutable............fs.add('ram')
print(len(s))
#print(s[2])
print(s)
#we can also define set like s=set()
print("-----------------------------")
s2=set()
for i in range(5):
  s2.add(i)
print(s2)
