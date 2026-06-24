#dictionaries
#creating dict
student = {
    'name' : 'Jeet',
    20 : 'Twenty',
    'hobbies' : ['photography','editing'],

}

#accessing dict
print(student.get('name'))
print(student)

#updating dict
student.update({
    'name' : 'Krishi'
})
print(student)


#dict()
a = dict(
    name = 'Frenny',
    age = '13'
)
print(a)
a.setdefault('place','Valsad')
a.setdefault('age',14)
print(a)

#delete

del a['age']
print(a)

place = a.pop('place')
print(place)

a ['hobby'] = 'Crochet'

print(a.get('name'))
print(a.keys())
print(a.values())
print(a.items())
#looping 
for keys,values in a.items():
    print(keys, '->', values)

 
#.fromkeys()
b = dict.fromkeys(['A','B','C'], 0)
c= dict.fromkeys(['A','B','C'])
print(b)
print(c)

#dict comprehension
sq = {i : i**2 for i in range(1,21) if i % 2 != 0}
print(sq)

#zip
j = [
    'a' , 'b'
]
k = [
    'c','d'
]
e = dict(zip(j,k))
print(e)
#dict as a counter
names = ['Harry','Hermoine','Ron','George','Fred','Ginny','Luna','Neville','Harry','Ron']
count = {}
for name in names:
    count[name] = count.get(name , 0) +1
print(count)    

counter = {}
for name in names:
    first = name[0] 
    counter[first] = counter.get(first,0) + 1
print(counter)    
#built in counter 
from collections import Counter
text = 'banana'
print(Counter(text))

print(Counter(names))