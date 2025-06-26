"""
creation of list objects
l=[]
l=[10,20,30]
l=eval(input("Enter List":)
l=list(sequence)
l=s.split(separator)
"""
#Traversing elements of list
l=eval(input("Enter List"))
for x in l:
    print(x)
print()
l=eval(input("Enter List"))
i=0
while i<len(l):
    print(l[i])
    i+=1
print("-----------------------------------------------")
l=list(range(0,21))
for x in l:
    if x%2==0:
        print(x)
print("-----------------------------------------------")
l=eval(input("Enter List"))
i=0
while i<len(l):
    print(l[i],"is at index {} and index {}".format(i,i-len(l)))
    i+=1
print("-----------------------------------------------")
"""
Functions and Methods
1.Function outside a class is known as function
2.Function inside a class is known as method
"""
#len.....this function used to return the length(size) of the list
l=[10,20,30,40,50,"Hari"]
print(len(l))
#count....used to return the occurrances of the list objects
l=[10,20,30,40,50,"Hari",10,10]
print(l.count(10))
#index....used to return list object based on index value of 1st occurance
l=[10,20,30,40,50,"Hari",10,10]
print(l.index(50))
#using membership operator
l=[10,20,30,40,50,60,10,20,10,80]
elem=input("Enter Element to search")
if elem in l:
    print(elem,"is found the at the ",l.index(elem))
else:
    print("Element is no found")
#Manupulating elements in the list
#append...used to add element at last position of list
l=[10,20,30,40,50]
(l.append(100))
print(l)
print("----------------------------------------------------")
l=[]
for x in range(101):
    if x%10==0:
        l.append(x)
print(l)
print("----------------------------------------------------")
#insert....used to add element at specific index
l=[10,20,30,40,50]
l.insert(0,100)
l.insert(50,1001)
print(l.index(1001))
print(l)
"""
Note:-while inserting we can mention more than max index,
it will taken as last index itself
*we can mention less than min index, arg will insert to 
starting index.
"""
#extend .....is used to add one list to another
l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2) #or..l3=l1+l2
print(l1)
#remove...used to delete the specific element
l1=[10,20,30]
l1.remove(10)
print(l1)
#while removing if the element is not avalilable in the list, it will throws an valueerror
l1=[10,20,30,4,50,60,70,80]
n=int(input("Enter element to remove:-"))
if n in l1:
    l1.remove(n)
    print("Element removed successfully--->",n)
    print(l1)
else:
    print("Element not available")
#pop....used to return and remove the last element,also remove element by index
l1=[10,20,30,40,50,60,70,80]
print(l1.pop(4))
print(l1)
"""
sort function used to sort element s in specific order
strings.....Alphabetical Order
integers....Ascending order
while sorting element all elements in the list are same type
"""
l1=[10,2,30,4,50,640,7,89]
l1.sort()
print(l1)
#reverse...used to return reverse order of sorting
l1=['z','d','n','k','r','p']
l1.sort(reverse=True)
print(l1)
"""
Creation of duplicates objects:
1.Aliasing:-
-----------------
*it is used to create different(duplicate) reference variable for same object
*suppose if we used to change change content in duplicate reference variable,
automatically in main variable also content will be change.
x=[10,20,30]
y=x
y.append(100)
y[0]=500
print(id(x))
print(id(y))
print(y)
print(x)
2.Cloning:-
--------------------
*it is used to defaultly will going to create a complete duplicate object
*cloning will be done by two ways
1.By using slice operator
x=[10,20,30]
y=x[:]
y.append(100)
y[0]=500
print(id(x))
print(id(y))
print(y)
print(x)
#by using slice we can copy element from specific range 
2.By using copy method
x=[10,20,30]
y=x.copy()
y.append(100)
y[0]=500
print(id(x))
print(id(y))
print(y)
print(x)
"""
"""
Comparing list objects:-
*Elements must be equal in both lists(== and !=)
*Content Should be same (including case)
*Order should be same
*Defaultly it will check the first element of the list.
*while checking in strings if 1st element is doesn't match it will go to second element 
strings(based on unicode)

x=[10,20,30]
y=[40,50,60]
print(x<y)


x=["Dog","Cat","Rat"]
y=["Dag","Cat","Rat"]
print(x>y)
print(ord("o"))
print(ord("a"))

"""
#clear...used to delete whole elements in the list
x=["Dog","Cat","Rat"]
x.clear()
print(x)
#Nested list....list inside another liat
x=[10,20,[30,40,50]]
print(x[0])
print(x[2])
print(x[2][0])
print(x[2][0:2])
print("------------------------------------------------------")
x=[[10,20,30],[40,50,60],[70,80,90]]
print(x[2][2])
for r in x:
    print(r)
print("------------------------------------------------------")
x=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=" ")
    print()
print("------------------------------------------------------")
#List Comprehensions
#syntax:-......list=[expression for x in sequence]
list=[x for x in range(0,11)]
print(list)
print("------------------------------------------------------")
l1=[x*x for x in range(0,11)]
l2=[x for x in l1 if x%2==0]
print(l1)
print(l2)
print("------------------------------------------------------")
vowels=['a','e','i','o','u']
word=input("Enter your word")
found=[]
for letter in word:
    if letter.lower() in vowels:
        if letter.lower() not in found:
            found.append(letter.lower())
print(found)
print("Number of vowels present in the",word,"is:",len(found))