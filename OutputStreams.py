#form-1...Blank line
print()
#form-2...printing strings
print("Hello Welcome to Python")
print("Harish"+"KR")
print("Harish","KR")
print("Harish"*3)
print("-----------------------------------------")
#form-3...print with variable number of aarguments
a,b,c=10,20,30
print(a,b,c)#defaultly it will printing with space
print(a,b,c,sep=":") #here sep keywors will separate values with specific argument
print("-----------------------------------------")
#form-4...with end attribute
#end attribute is used to print statements in same line with specific argument
print("Harish",end="-")
print("KR",end="-")
print("Hindupur",end="-")
print("Andhra Pradesh")
print("-----------------------------------------")
#form-5....print any kind of objects
l=[10,20,30]
s={10,20,30}
t=(10,20,30)
print(l,end="-")
print(s,end="-")
print(t)
print("-----------------------------------------")
#orm-6...formatted String
a="Harish"
b=25
c="Hindupur"
print("Hi,i am %s age of %i and i am from %s"%(a,b,c))
print("-----------------------------------------")
#form-7....#replacement operator{}
a="Harish"
b=25
c="Hindupur"
print("Hi,i am {} age of {} and i am from {}".format(a,b,c))
print("Hi,i am {0} age of {1} and i am from {2}".format(a,b,c)) #by index values
print("Hi,i am {x} age of {y} and i am from {z}".format(z=c,y=b,x=a))