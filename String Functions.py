'''strip keyword is used to trim the spaces of the string
we have 3 types strips lstrip...rstrip...strip
'''
"""
l=["Hyderabad","Chennai","Bangalore","Delhi"]
s=input("Enter the city:-")
if s.strip() in l:
    print("Your city is available")
else:
    print(s,"is not available,enter the valid one")"""
print("----------------------------------------------------")
"""print("Forward Direction String")
s=input("Enter String:-")
n=len(s)
i=0
while i<n:
    print(s[i],end="-")
    i+=1
print("----------------------------------------------------")
print("Backward Direction String")
s=input("Enter String:-")
n=len(s)
i=n-1
while i>=0:
    print(s[i],end=' ')
    i-=1
print("---------------------------------------")
s=input("Enter String:-")
n=len(s)
i=-1
while i>=-n:
    print(s[i],end=' ')
    i-=1"""
print("---------------------------------------")
"""#comparison of the strings

s1=input("Enter first string:-")
s2=input("Enter Second String:-")
if s1==s2:
    print("Both strings are equal")
elif s1>s2:
    print("String1 is bigger than s2")
else:
    print("s1 is smaller than s2")

Note:- while checking comparison of strings will be based unicode of alphabets
"""
print("---------------------------------------")
#count...used the strings...in python single character will be trated as string
"""
s="abaabbababbaa"
s1=s.count("a",0,len(s))
print(s1)
"""
print("---------------------------------------")
"""
#Replacing string element with new string element
s="Leraning python is very difficult"
print(s)
s1=s.replace("difficult","easy")
print(s1)
"""
print("---------------------------------------")
s="abababababababababa"
print(s)
print(id(s))
s1=s.replace("b","a")
s2=s.replace("a","b",4)
print(s1)
print(id(s1))
"""Note:-strings are immutable it cant change the string object
while changing string object old one will go to garbage collection,
then new object will create for thst reference."""
print("---------------------------------------")
#Splitting if strings
#we can split the string by using separartor, default spearator is space
"""d="06-02-2024"
d1=d.split("-")
print(d1)
for l in d1:
    print(l)

#split string up to specific index
s="Harish KR Hindupur Aanatapur Andhra"
print(s.split(" ",2))
for l in s:
    print(l,end="")"""
#Note:-split up to 2 index rest of the elements as one string
#Note-split can split strings and make it as a "list
#rsplit... same as split but it will split elements in reverse order
print("---------------------------------------")
#join...this function join elements of a sequence and make it a string with a spearator
l=["Harish","KR","Hindupur","Anantapur"]
l1="-".join(l)
print(l1)
print("---------------------------------------")
#changing case of string
"""s="Harish KR Hindupur Aanatapur Andhra"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())"""
print("---------------------------------------")
#checking starting and ending part of string
"""s="Harish KR Hindupur Aanatapur Andhra"
print(s.startswith("Harish"))
print(s.endswith("Andhra"))"""
print("---------------------------------------")
"""print('Durga786'.isalnum())
print('durga786'.isalpha()) #False
print('durga'.isalpha()) #True
print('durga'.isdigit()) #False
print('786786'.isdigit()) #True
print('abc'.islower()) #True
print('Abc'.islower()) #False
print('abc123'.islower()) #True
print('ABC'.isupper()) #True
print('Learning python is very easy'.istitle()) #False
print("Learning Python Is Very Easy".istitle()) #True
print(" ".isspace()) #True
print("Durga Soft Solutions".isspace())
print("123".istitle())"""
print("---------------------------------------")
#Forms of reverse a string
#form-1 using slice operator
"""s="HarishKR"
print(s[::-1])
#form-2 using reversed key word
s=input("Enter String")
for x in reversed(s):
    print(x)

s=input("Enter String")
print("".join(reversed(s)))

#form-3...
s=input("Enter String")
i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1
#form-4....
s="Harish KR Hindupur Aanatapur Andhra"
l=s.split()
i=len(l)-1
l1=[]
while i>=0:
    l1.append(l[i])
    i-=1
print(l1)
print(" ".join(l1))
#form-5.....
s="Harish KR Hindupur Aanatapur Andhra"
l=s.split()

l1=[]
for x in l:
    l1.append(x[::-1])
print(l1)
print("-".join(l1)"""
print("---------------------------------------")
#Even and odd positions of the string
s=input("Enter String:-")
print("Even Positions",s[::2])
print("Odd Positions",s[1::2])

s=input("Enter String")
print("Even Positions")
i=0
while i<len(s):
    print(s[i],end="")
    i+=2
print()
print("Odd Positions")
i=1
while i<len(s):
    print(s[i],end=" ")
    i+=2
print("---------------------------------------")
#Using sort function...sort integral and alphabet values
s=input("Enter String:-")
s1=s2=output=""
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
for x in sorted(s2):
    output=output+x
print(output)
print("---------------------------------------")
#Repeat alphabet as per next number...a4...aaaa
s=input("Enter String")
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+previous*(int(x)-1)
print(output)
print("---------------------------------------")
#Get character using unicode...chr(unicode)
print(chr(111))
#ord()...this function is used to convert unicode character into integral representation
print(ord("a"))
print("---------------------------------------")
#a4k3b2.....aeknbd
s=input("Enter String:-")
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        newch=chr(ord(previous)+int(x))
        output=output+newch
print(output)
print("---------------------------------------")
#s1=Nandi....s2=Hari....NHaanrdii
s1=input("Enter String")
s2=input("Enter String")
i=j=output=0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i+=1
    if j<len(s2):
        output=output+s2[j]
        j+=1
print(output)
print("---------------------------------------")
s1=input("Enter String:-")
s2=input("Enter String:-")
i=j=0
output=""
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i+=1
    if j<len(s2):
        output=output+s2[j]
        j+=1
print(output)
print("---------------------------------------")
#Remove Duplicates in present string
s=input("Enter String")
l=[]
for x in s:
    if x not in l:
        l.append(x)
print("-".join(l))
print("---------------------------------------")
#using Dictionary
s=input("Enter String")
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else:
        d[x]=d[x]+1
for k,v in  d.items():
    print("{} occurs {} times".format(k,v))
print(d.items())



