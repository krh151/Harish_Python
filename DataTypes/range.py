#range.....represents the sequence of values....immutable
r=range(5)
for i in r:
    print(i)
print(r[3])
print(r[0:3])
print(r)
#immutable..............r[3]=100
print("-----------------------------")
for i in range(10,15):
    print(i)
print("-----------------------------")
#int type doesnt support indexing or slicing..........print(i[2])
for i in range(10,30,5): #increment by 5
    print(i)
#Note:-range doesnt allow float values




