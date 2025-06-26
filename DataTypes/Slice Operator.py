#Syntax....a[Begin of index value:End of index value]
a='HarishKR'
#print(a[1])
#Below statment returns starting from 1st index and with 5thindex-1
print(a[1:5])
#---------------------
print(a[2:])
print(a[:3])
print(a[:])
print(a[-7:-3])
#Skipping elements in a string
print(a[0:7:3]) #Here 3 means it will skip 2 elements from beginning index
"""
Note:-
*if step is positive...it will be forward direction
begin to end-1
*if step is negative...it will be backward direction
begin to end+1
*End should not be -1 or end+1 is 0....then result is always empty string
"""