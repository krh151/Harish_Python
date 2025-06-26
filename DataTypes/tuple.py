#same as list but only only difference...tuple is immutable
t=(10,'Hari',True,10+20j,10)
#immutable.........t.append('ram')
print(len(t))
print(t[2])
print(t[0:2])
print(t)
print("------------------------------------------------------")
#valid tuples
t=()
t=10,20,30
t=10,
t=(10,)
t=(10,20,30)
print(t)
print("------------------------------------------------------")
list=[10,20,30]
t=tuple(list)
print(t)

t=tuple(range(1,11))
print(t[0])
print(t)

t=tuple(range(1,11))
t1=100,200,300
t2=t1+t
print(t2)
print("------------------------------------------------------")
#Tuple functions(len,count,sorted,reverse)
t=tuple(range(1,11))
print(len(t))

t=(10,20,30,10,10)
print(t.count(10))

t=(50,80,66,35,10,20,30,10,10)
print(sorted(t)) #while implementing sorted function in tuple, defaultly it will return as list type

#return tuple type while using sorted function as follows
t=(50,80,66,35,10,20,30,10,10)
print(tuple(sorted(t)))

t=(50,80,66,35,10,20,30,10,10)
print(tuple(sorted(t, reverse=True)))
print(min(t))
print(max(t))
#tuple packing...means add multiple elements in one list
a=10
b=20
c=30
t=a,b,c
print(t)
#tuple unpacking....means it is quite opposite packing
t=10,20,30
a,b,c=t
print(a,b,c)

t=eval(input("Enter some tuple"))
l=len(t)
sum=0
for x in t:
    sum=sum+x
print("Sum:-",sum)
print("Average:-",sum/l)

"""
tuple comprehension not supports,it will just generator class or type
t=(x*x for x in range(1,11))
print(t)
"""