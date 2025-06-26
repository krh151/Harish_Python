#Special Operators....used to compare the references of objects (is, is not)
a=10
b=10
print(id(a))
print(id(b))
print(a is b)
print( a is not b)
#Note:-Here a,b are int variables we cant change(immutable),variables belongs to same object.
print("-------------------------------------")
x=[10,20,30]
y=[10,20,30]
print(x is y)
print(x is not y)
print(x==y)   #it is only compare the content
#Here variables are list type thos are mustable that why the doesn't belongs to same object