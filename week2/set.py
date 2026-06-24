s = set(
    [1,2,2]
)
print(s)

se = {
    1,2,3,4,4,4,3
}
print(se)

se.add(5)
print(se)

se.remove(1)
print(se)

print(s.intersection(se))
print(s & se)

print(s.difference(se))
print(s - se)

print(s.union(se))
print(s | se)

print(s.symmetric_difference(se))
print(s ^ se)
# s = {
#[1,2,3,4,5,5]
#
# print(s) error-- lists are unhashable 

a = {'A','B'}
b = {'C','D'}

a |= b
#a.update(b)
print(a,b)

a.difference_update(b)
print(a,b)
# a-= b
#multiple arguments
# a-=[|b|c...]

a.intersection_update(b)
#a &= b
print(a,b)

a.symmetric_difference_update(b)
# a ^= b
print(a,b)

fs = frozenset([1,2,3,4,4,4,5])
print(fs)

import time
start = time.time()
a = print('hellooooo jeeet')
end = time.time()
print(end - start)

print('helloo')
time.sleep(3)
print('bye')


#deduplicating list while preserving order 
words = ['hi','bye','mango','jeet','jeet','mango']
unique = []
s = set()

for word in words:
    if word not in s:
        s.add(word)
        unique.append(word)
print(unique)   
     
#given a list of lists find duplicate lists
a = [
    [1,2],
    [3,4],
    [5,6],
    [3,4],
    [5,6]
]
seen = set()
dup = set()

for item in a:
    t = tuple(item)
    if t in seen:
        dup.add(t)
    else:
        seen.add(t) 
print(dup)            