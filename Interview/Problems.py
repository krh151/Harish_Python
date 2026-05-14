"""
1.Decorators -Decorators are functions that modify the behavior of another function without changing its code.
A decorator is a function that wraps another function to add extra behavior without modifying its original code.

def log(func):
    def wrapper():
        print("Executing")
        func()

    return wrapper

@log
def hello():
    print("Learning Decorators")
#hello = log(hello)
hello()
----------------------------------------------------------------

2. Reverse a String
Here format is start:end:step for slicing the string -1 means takes from right to left suppose -2 means takes every 2
character and positive numbers 1 2 takes from left to right of the string
step means how amy position of the character
s = "hello"
print(s[::-1])
----------------------------------------------------------------

3. Palindrome

s='Malayalam'
s=s.lower()
if s==s[::-1]:
    print("Palindrome")

-------------------------------------------------------------------

4.Count frequency of characters
s = "testtt"
freq = {}
for c in s:
    freq[c] = freq.get(c, 0) + 1 #Here get is used to prevent key error if key doesn't exist
print(freq)

s="testt"
freq={}
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

-----------------------------------------------------------------------

5.Remove duplicates
l = [1,2,2,3]
print(list(set(l)))

l = [1,2,2,3]
res = []
for i in l:
    if i not in res:
        res.append(i)

print(res)

-------------------------------------------------------------------------

6. Find largest number in list

s=[1,2,3,2,2,2,2,55555]
print(max(s))

7. find Vowels

s="hello"
count=0
vowels=[]
for i in s:
    if i in "aeiou":
        count += 1
        vowels.append(i)
print(vowels)
print(count)

8. Swap Numbers
a, b=5, 10
a, b= b,a
print("a:", a, "\n" "b:", b)

9.Find the 2nd largest number
l = [1,5,3,9]
l = list(set(l))
l.sort()
print(l[-2])

10.Rotate an array
arr = [1,2,3,4,5,6,7]
k = 2
k = k % len(arr) # here it is for safe side to handle the rotation properly suppose if ki bigger than array length
result = arr[-k:] + arr[:-k]
print(result)

11. Python code to validate API response

import requests
res = requests.get("https://dummyjson.com/products")
assert res.status_code == 200
print(res.status_code)
data = res.json()

# Access the 'products' key and print the 'title' of the first item
print(data['products'][2]['title'])

12.Sample pytest case

def test_add():
    assert 2+2 == 4

def test_get_products_status():
    res = requests.get("https://dummyjson.com")
    print("\n")
    print(res.status_code)
    assert res.status_code == 200

def test_first_product_title():
    res = requests.get("https://dummyjson.com/products")
    data = res.json()
    print("\n")
    print(data['products'][2]['title'])

"""