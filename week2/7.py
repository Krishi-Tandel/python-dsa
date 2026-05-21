'''
Flattening Manually vs Comprehension
Given:
pythonnested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
First flatten it using a nested for loop the traditional way. 
Then do the exact same thing with a nested list comprehension in one line. 
Print both and confirm they match. 
'''
pythonnested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lst = []
for rows in pythonnested:
    for n in rows:
        lst.append(n)
print(lst)

lst1 = [n for rows in pythonnested for n in rows]
print(lst1)

is_True = bool(lst == lst1)
print(is_True)