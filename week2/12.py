student = dict(
    name = "Jeet",
    age = 21,
    hobbies = ['Photography', 'editing'],
    place = 'Valsad'
)

print(student['hobbies'][0])

print(student.get('hobbies' [3],'not found'))

print(len(student))

print(student.keys())
print(student.values())
print(student.items())

for keys,value in student.items():
    print(keys , '-> ', value)

