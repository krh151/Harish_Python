#Type Casting used to convert one datatype to another datatype,we have different functions as follows
#int Function.....int()
print(int(156.67)) #Float
print(int(True)) #bool
print(int("309")) #String must in decimal form while converting to int with base10
#while converting str to int string value should not float......print(int("23.44"))
#Complex type is not possible to convert to int.....print(int(10+20j))
#Int forms also not able to convert.......print(int(0b111)) #Binary int form

print("__________________________________________________________")
#Float function.......float()
print(float(156.67)) #Float
print(float(156)) #Decimal
#complex not able to convert........print(float(10+20j)) #Complex
print(float("234")) #string must be in form of decimal
print(float(True)) #bool
#Int forms also not able to convert.......print(float(0b111)) #Binary int form
#This type of string not able to convert........print(float("Ten))

print("__________________________________________________________")
#Bool Function bool()
#this function will convert all data types to bool
print(bool(123))
print(bool(0))
print(bool(10+34j))
print(bool("222"))
print(bool(12.77))

print("__________________________________________________________")
#Complex Function......complex()
print(complex(2))
print(complex(2,3))
print(complex("10"))
print(complex(10.34))
print(complex(True))
#This type of string not able to convert........print(complex("Ten))
#Int forms also not able to convert.......print(complex(0b111)) #Binary int form

print("__________________________________________________________")
#String Function.....str()
#it will convert all types to string
print(str(20))
print(str(20+30j))
print(str(20.656))
print(str(True))








