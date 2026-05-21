
student = dict(
        name ='Krishi',
        age =20,
        courses = ['Math', 'Science'],
)
print(student.get('name'))
print(student.get('place', 'Not found'))
print(student.items())

for key,value in student.items():
    print(key,value)

a = {
    10 : 'a',
    True : 'yes',
    ('a','b') : 'tuple'  # can use tuple but not lists, sets or dict as keys
}
print(a)

#values have no restriction whatsover

#using zip()
a = ['name','age','place']
b = ['Krishi',20,'Valsad']

print(dict(zip(a,b)))

# .fromkeys() class method
# default value for all keys
student = dict.fromkeys(['A','B','C'], 0)
print(student)