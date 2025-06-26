'''strip keyword is used to trim the spaces of the string
we have 3 types strips lstrip...rstrip...strip
'''
l=["Hyderabad","Chennai","Bangalore","Delhi"]
s=input("Enter the city:-")
if s.strip() in l:
    print("Your city is available")
else:
    print(s,"is not available,enter the valid one")
