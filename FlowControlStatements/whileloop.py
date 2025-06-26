#n=int(input("Enter Number:-"))
i=0
while i<10:
    i+=1
    print(i,end=" ")
print("---------------------------")
#sum of n numbers
n=int(input("Enter Number:-"))
sum=0
i=1
while i<n:
    sum+=i
    i+=1
print(sum)
print("---------------------------")
name = input("Enter Username:-")
pwd = input("Enter Password:-")
while name != "Hari" or pwd != "python":
    print("Your are entered incorrect details, try it again")
    name = input("Enter Username:-")
    pwd = input("Enter Password:-")

print("Thanks for your credentials")


