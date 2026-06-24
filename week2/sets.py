#Basic Set Creation
s = {1,2,3,4,5}
print(type(s))

j = [1, 2, 2, 3, 3, 4, 5]

ss = set(j)
print(ss)
print(type(ss)) #duplicates are removed

#empty set 
k = set() # k ={} creates an empty dict

#add,remove,discard
a = {10, 20, 30}
a.add(40)
a.remove(20)
a.discard(50)
#a.remove(50) gives error while a.discard() ignores as 50 doesnt exist in set
print(a)

a.pop()
print(a)
#membership testing
f = {10, 20, 25, 30}
print(25 in f)
#Count how many numbers from a list exist in a set.
nums = [1,2,3,4,5]
lookup = {2,4,6,8}
count = 0
for num in nums:
    if num in lookup:
        count += 1
print(count)

#union 
c = {1,2,3}
b = {3,4,5}
d = {6,5,4}
print(c | b | d)
#or
print(c.union(b,d))
#intersection or &
e = {1,2,3,4}
f = {3,4,5,6}
print(e.intersection(f))

#Find students enrolled in both courses.
python_students = {"A","B","C","D"}
web_students = {"C","D","E","F"}
print(python_students & web_students)

#difference
print(e.difference(f))
print(f.difference(e))
# or -
#symmetric difference

q = {1,2,3}
r = {3,4,5}
print(q.symmetric_difference(r))
#or ^

#Find all unique elements between two lists using only set operations.
l1 = [1,2,3,4]
l2 = [3,4,5,6]

l = set(l1)
ll = set(l2)

print(l.symmetric_difference(ll))

#deduplication
d = [10,20,10,30,20,40]
dup = set(d)
print(dup)

#Count unique elements in a list.
u = [10,20,10,30,20,40]
n = set(u)
print(len(n))

#Check if a list contains duplicates.
num = [1,2,3,2]
dupl = set(num)

if len(num) != len(dupl):
    print("Duplicates found")
else:
    print("Duplicates not found")    

#frozenset
fs = frozenset([1,2,2,3,3])
print(type(fs))
#fs.add(10)-- error, cannot add or modify elements in frozenset
fs1 = frozenset(
    {'name' : 'Krishi',
     'age' : 20
    }
)
print(fs1)

#Find common elements between two lists using only set operations.
a = [1,2,3,4,5]
b = [4,5,6,7]
s1 = set(a)
s2 = set(b)
print(s1.intersection(s2))

#Find elements unique to the first list
print(s1 - s2)
print(s2 - s1)

print(s1 ^ s2)
#Count unique email addresses.
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com",
    "c@gmail.com",
    "b@gmail.com"
]
email1 = set(emails)

print(len(email1))


