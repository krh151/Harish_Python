'''while finding substrings we have functions like
find, rfind
index rindex
'''
'''...."find"...is used serach the specific portion of string
from left to right and return the first occurrence
if the string found it just return it's index value
string not found .. returns 0
'''
s="Harishkr"
print(s.find("kr"))
s1="harishkrhindupur"
print(s1.find('h',6,10))
'''
print("-----------------------------------")
...rfind... is used to find string from right to left
it will calculate the index of reverse of string
'''
a="harishkr"
print(s.rfind("r"))
a1="kurubaharish"
print(a1.rfind('a',4,11))

print("-----------------------------------")

"""
index... same as find but only difference is if the string is not 
available it raise an value error while using indexes

s2="Harishkr"
print(s.rindex("krk"))"""
'''print("-----------------------------------")
print("using exception handling for indexes to prevent errors")
mstr=input("Enter main string:-")
sstr=input("Enter sub string:-")
try:
    n=mstr.index(sstr)
except ValueError:
    print("sub string is not found in the main string")
else:
    print("sub string is found")
print("Index value is:-", n)'''
print("-----------------------------------")
print("print all the position of substring availability not 1st occurrence")
ms=input("Enter main string:-")
ss=input("Enter sub string:-")
flag=False
pos=-1
n=len(ms)
count=0
while True:
    pos=ms.find(ss,pos+1,n) #Here pos will asssigning the value of founded index
    if pos==-1:
        break
    flag=True
    count+=1
    print("sub string is found at the index:=",pos)
if flag==False:
    print("sub string not found")
print(count)


