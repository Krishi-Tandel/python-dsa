# Exercise 1: deduplicate a list while preserving order
# (set alone loses order — how do you solve this?)
words = ["banana", "apple", "banana", "cherry", "apple", "date"]
unique = []
s = set()
for word in words:
    if word not in s:
        s.add(word)
        unique.append(word)
print(unique)
# Exercise 2: use a tuple as a dict key (lists can't be dict keys)
# use frozenset as a dict key — when would this be useful?
a = {
    (1,2) : ('A'),
    (2,3) : ('B')
}
print(a)

a = {
    frozenset(['read', 'write']) : 'editor',
    frozenset(['read']) : 'viewer'
}

# Exercise 3: given a list of lists, find duplicate sublists
a = [
    [1, 2],
    [3, 4],
    [1, 2],
    [5, 6],
    [3, 4]
]
seen = set()
duplicates = set()  

for item in a:
    frozen = frozenset(item)
    if frozen in seen:
        duplicates.add(frozen) 
    else:
        seen.add(frozen)

print(duplicates)      
print(seen) 
