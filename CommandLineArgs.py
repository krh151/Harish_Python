#Command Line Arguments
"""
Arguments thar are getting from the cmd
defaultly argv will be a type of list variable
argv holds values as we passed (arguments)
"""
#from sys import argv
#print(type(argv))
from sys import argv
print(len(argv))
print(argv)

print(type(argv))
print("---------------------------------------")
#print sum of arguments
from sys import argv
sum=0
for x in argv[1:]:
     n=int(x)#need to convert int type, internally it was in str type
     sum=sum+n
print(sum)
print("---------------------------------------")
"""import sys
print(sys.argv[4])
print("---------------------------------------")
import sys
print(sys.argv[6])"""
#Note:- if we want make multiple str arguments as one arg should keep it in quotes
#print sumthrough cmd
from sys import argv
print(int(argv[1])+int(argv[2]))







