#del keyword is used to delete the objects
x=20
print(x)
print("-----------------------------")
'''x=20
del (x)
print(x)'''
#None... datatype is used to define a null to a variable
#it will returns nothing
a=10
b=20
print(b)
print("-----------------------------")
a=10
b=20
b=None
print(type(b))
print(b)
print("-----------------------------")
#if multiple references have same objects,it will specific reference of the object
s1="Hari"
s2="Hari"
s3="Hari"
del (s1)
print(s2)
print(s3)


