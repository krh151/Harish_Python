#bytes.....it represent the group of byte numbers just like an array
a=[10,20,30,40,50]
b=bytes(a)
print(type(a))
print(b[4])
#.....it is immutable b[0]=100
for i in b:
    print(i)

print("---------------------------------------")
#bytearray same as byte but it is mutable
x=[100,200,30,40,50]
y=bytearray(x)
print(type(y))
print(b[4])
y[0]=12
#.....it is immutable b[0]=100
for i in y:
    print(i)

#Note:- while using these types byte numbers must be in range of 0-256