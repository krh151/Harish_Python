#break...this statement  used to terminate entire iteration if the condition if false
for i in range(11):
    if i==7:
        break
    print(i)
print("------------------------------------")
price=[50,80,65,200,95,20]
for rates in price:
    if rates>100:
        print("{} is high price".format(rates))
        break
    print("{} is ok".format(rates))