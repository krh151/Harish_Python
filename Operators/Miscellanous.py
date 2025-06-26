#Leftshift Operator
"""
Means it will cancel the left side 2 bits what we are taken as input,
and add to the right side
"""
print(10<<2) #00000000000....001010
#Rightshift Operator
"""
Means it will cancel the right side 2 bits what we are taken as input,
and add to the left side 
"""
print(-10>>2) #00000000000....001010
"""
Note:- Here +ve 10 means in vacant cells it will taken as 0
            -ve 10 menas in vacnt cells it will taken as 1
"""
print("__________________________________________")
#++x means it will treated as +(+x)
x=10
print(++x)
#print(x++).....its not avaibale in python
print("__________________________________________")
"""
Ternary Operator:- its is nothing but conditional statement
"""
a,b,c=100,200,30
print("Correct" if a<b else "Not Correct")
Max=print("Max is",a if a>b and a>c else b if b>c else c)
print("__________________________________________")
a=[10,20,30]
b=[10,20,30]
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
#Note:- Here both ids are different because of list mutable
print("__________________________________________")
a, b=10,10
print(id(a))
print(id(b))
print(a is b)
"""Note:- Here both ids are same because of integer is immutable 
(not possible to change objects) all references will have same objects,"""
print("__________________________________________")
#Special Operators.....1.Identitiy Operators(is, is not)
#This operators will compare the object references
a,b=10+3j,(10+3j)
print(a is b)
print(a is not b)
print("__________________________________________")
#2.Membership Operators...these are used to check whether the element is present or mot(in, not in)
a=[10,20,30,40]
print(10 in a)
print(88 not in a)
print("__________________________________________")
"""
Taking multiple values from user at a time by using split function
(will break entire string into individual elements based on argument that passed in split function)
"""
#a,b=[int(x) for x in input("Enter 2 numbers").split()]
#print("Result",a+b)
#Note:-.....This approach is for only int values
print("__________________________________________")
"""
eval()
This function used to evaluate expression as a string return value as integer
No need to specify type to any value, it will automatically identifies
"""
a=eval("10+20*30/40")
print(type(a),a)
a,b,c,d,e=[eval(x) for x in input("Enter Values").split()]
print(type(a))
print(type(c))
print(type(d))
print(type(e))
print(a+b)