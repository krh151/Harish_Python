for i in range(10):
    print(i,end=" ")
print()
for i in range(1,11):
    print(i)
print("--------------------------")
n=int(input("Enter Number:-"))
sum=0
for i in range(n):
    sum+=i
s=sum*sum
print(s)
print("--------------------------")
#Nested forloop
for i in range(4):
    for j in range(4):
        print("{0} of {1}".format(i,j))
print("---------------------------")
n=int(input("Enter Number"))
for i in range(1,n+1):
     for j in range(1,i+1):
        print("* ",end=" ")
     print()
print("---------------------------")
n=int(input("Enter Number"))
for i in range(n):
    print("*"*i)
print("---------------------------")
n=int(input("Enter Number:-"))
for i in range(1,n+1):
        print("* "*n)
print("---------------------------")
n=int(input("Enter Number:-"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()











