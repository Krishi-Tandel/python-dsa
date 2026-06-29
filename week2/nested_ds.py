#list of dict
students = [
   {'name' : 'Jeet', 'marks' : 90, 'Section' : 'A' },
   {'name' : 'Krishi', 'marks' : 80, 'Section' : 'A' },
   {'name' : 'Arjun', 'marks' : 70, 'Section' : 'B' }
]

for student in students:
    print(student['name'], student['marks'])

#sorting
sorted_students = sorted(students, key = lambda s : s['marks'], reverse=True)
print(sorted_students)

#filtering
print(list(filter( lambda student: student['marks'] >= 80, students)))

# sort by multiple keys: section first, then grade descending
s = sorted(students, key = lambda s: (s['Section'], - s['marks'] ))
print(s)