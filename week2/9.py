#dictionaries
student = {'name' : 'Jeet', 'age' : 20, 'courses' : ['Math', 'Sci']}
print(student.get('name'))
student.update({'name': 'Krishi'})
del student['age']
print(student)