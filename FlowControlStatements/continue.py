#continue....this statement is used to skip the current iteration of the loop
for i in range(11):
    if i==7:
        continue
    print(i)
print("------------------------------------")
price=[50,80,65,200,95,20]
for rates in price:
    if rates>100:
        print("{} is high price".format(rates))
        continue
    print("{} is ok".format(rates))
print("------------------------------------")
#for-else...while using for else...else part is executed only if the loop without break
price=[50,80,65,200,95,20]
for rates in price:
    if rates>500:
        print("{} is high price".format(rates))
        continue
    print("{} is ok".format(rates))
else:
    print("All rates are ok")
