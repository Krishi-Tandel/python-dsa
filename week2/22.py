list1 = ["apple", "banana", "cherry", "date"]
list2 = ["banana", "date", "elderberry", "fig"]
s1 = set(list1)
s2 = set(list2)
# Task 1: elements common to both lists
print(s1 & s2)
print(s1.intersection(s2))

# Task 2: elements unique to list1 only
print(s1 - s2)
print(s1.difference(s2))

# Task 3: elements unique to list2 only
print(s2 - s1)
print(s2.difference(s1))

# Task 4: all unique elements combined (no duplicates)
print(s1 | s2)
print(s1.union(s2))

# Task 5: elements that are in one list but NOT both
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

# Use ONLY set operations — no loops, no if statements

