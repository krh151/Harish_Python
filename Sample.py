from random import *
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9), sep='')
def hari():
    for i in range(11):
        print(i)
hari()
a=10
a=True
print(type (a))

a1="HUP"
a2="HUp"
a3="HUP"
a4="HUP"
print(id(a1),id(a2),id(a3),id(a4))
print(a1 is a3)
print("------------------------------------------------")
#is keyword is used to compare to references(id) of the object
x=257
y=257
print(x is y)
x1=10.0
x2=10.0
print(x1 is x2)
p=10+20j
q=10+20j
print(p is q)
print("------------------------------------------------")
a=eval(input("Enter Some data"))
print(type(a))

