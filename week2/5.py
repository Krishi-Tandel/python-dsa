'''
Uppercase Filter
Given names = ['alice', 'bob', 'charlie', 'diana', 'eve'], use a list comprehension to:
Uppercase every name
Keep only names with more than 3 letters, uppercased
Create a list of tuples (name, len(name)) for all names
'''
names = ['alice', 'bob', 'charlie', 'diana', 'eve']

uc = [item.title() for item in names ]
print(uc)

le = [n for n in uc if len(n) > 3]
print(le)

tup = [(name,len(name)) for name in uc]
print(tup)