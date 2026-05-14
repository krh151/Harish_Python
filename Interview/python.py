"""
Data Types

1.List
l=[1,2,3,4,5]
print(type(l))
l[0]=100
l.append(1000)
l.insert(2, 55)
print(l)

2.Tuple
t=(1,2,3,4,5)
print(type(t))
t=t+(100,)  #Not changing creating new one
# not mutable as below
# t[0]=100
# t.append(1000)
# t.insert(2, 55)
print(t)

3.Set
s={1,2}
s.add(20)
#print(s[0]) #Coz set is unordered
print(s)

4.Dictionary
d={"name":"Hari", "phone":123}
print(d)
print(d["name"])
d["name"]="jhjfh"
d["address"]="xxx"
print(d)

5.Generator
Is a function returns a values one by one using yield instead of returning all the values at once
uses the keyword yield instead of return

def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()

print(next(g))
print(next(g))
print(next(g))

def count(n):
    for i in range(n):
        yield i
for num in count(3):
    print(num)


6.Lambda Function
A lambda function is an anonymous, one-line function used for short operations without defining a full function using def.”
lambda arguments : expression

add=(lambda a,b:a+b)
print(add(2,3))

data=[(1,1),(1,0),(1,2)]
result=sorted(data, key=lambda x:x[1])
print(result)

l=[1,2,3,4]
res=list((map(lambda c:c*2, l)))
print(res)

l=(1,2,3,4)
r=tuple((filter(lambda x:x%2==0, l)))
print(r)

What is List Comprehension?
List comprehension is a short and clean way to create lists using a single line of code.
l=[1,2,3,4]
res=[i*i for i in l]
print(res)

l=[1,2,3,4, 9, 16, 20 ,11]
even=[i for i in l if i %2==0]
print(even)

Shallow vs Deep copy
“Shallow copy creates a new outer object but shares inner objects,
while deep copy creates completely separate copies of all nested objects.”

Shallow Copy-
Shallow copy copies only the outer object
Nested objects are still shared
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 100
print(a)
print(b)

---------------------------------------------------------------

Deep copy-
Deep copy copies everything completely
No shared nested objects
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 100
print(a)
print(b)

What is Exception Handling?
Exception handling is used to handle runtime errors gracefully without stopping the program.
using try, catch, finally and else blocks

try: #risky code
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

except ZeroDivisionError: #handling error
    print("Cannot divide by zero")

except ValueError: #handling error
    print("Please enter valid numbers")

else:
    print("Division successful")
    print("Result:", result)

finally: #always run
    print("Program execution completed")

OOPs Object-Oriented Programming concepts -
OOP (Object-Oriented Programming) in Python is a programming style where we organize code using:
classes, objects to represent real-world entities.

1.Class - A class is a user-defined blueprint or template for creating objects.
It defines a set of attributes (variables) and methods (functions)
that all objects created from it will have.

2.Object -An object is a specific instance of a class.
While the class is the blueprint, the object is the actual building constructed
from that blueprint. It holds real values (instance variables) and
can perform actions defined in its class

class Car:
    brand = "BMW"
    def start(self, new_brand):
        self.brand=new_brand
        print("Car Started")
car1=Car()
car2=Car()
car1.start("Audi")
print(car1.brand)
print(car2.brand)

3.Inheritance - One class acquires properties and methods of another class.

class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def bark(self):
        print("Dog Barks")

d=Dog()
d.sound()
d.bark()

Dog class inherited Animal class features.
Benefits of Inheritance
code reuse
less duplication
better maintenance

4.Encapsulation - Hiding important data from direct access
and allowing access only through controlled methods.

class Bank:
    def __init__(self):
        self.__balance = 1000
    def get_balance(self):
        return self.__balance
b=Bank()
print(b.get_balance())

===============================================================

class Employee:
    def __init__(self):
        self.__salary = 50000
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
    def get_salary(self):
        return self.__salary

e = Employee()
e.set_salary(70000)
print(e.get_salary())

Note:- __balance means variable becomes private no direct access
Benefit - To protect sensitive data
__init__ - it is a special method it runs automatically when object is created

class Student:
    def __init__(self):
        print("Constructor Called")
s=Student()

Why Use __init__?
Used to:
initialize variables
assign values
setup object data

Note- The self parameter is used to represent the specific instance of the class.
It serves as a bridge that allows methods to access and modify the data (attributes)
belonging to that particular object.

self is used to access variables and methods belonging to the current object.

4.Polymorphism - Same method behaves differently in different classes.

class Cat:
    def sound(self):
        print("Meow")
class Dog:
    def sound(self):
        print("Bark")

c=Cat()
d=Dog()
c.sound()
d.sound()

5.Abstraction - Showing only important details and hiding implementation.
Hiding implementation details and showing only essential functionality.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("Ignition setting Up")
class Car(Vehicle):
    def start(self):
        print("Car Started")

c=Car()
c.start()

"""

