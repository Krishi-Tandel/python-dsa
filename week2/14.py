
#.update()
dict1 = {
    'name' : 'Jeet',
    'age' : 21,
    'degree' : 'Btech Mechanical'
}

dict2 = {
    'hobbies' : ['photography','editing'],
    'place' : 'Valsad' 
    }

dict1.update(dict2)
print(dict1)

# dict and a seq of key value pair
dict1.update([('a','b')])
print(dict1)

# dict and keywords args
dict1.update(age = 22)
# using |
updated = dict1 | dict2
print(updated)

#remove keys

dict1.pop('place')
print(dict1)

del dict1['age']
print(dict1)

a = dict1.copy()
print('Copied', a)

dict1.clear()
print(dict1)

# **
res = {**dict1, **dict2}
print(res)
