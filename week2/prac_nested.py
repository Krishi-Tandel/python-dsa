# #list of dict
# #1. Print all student names
# #2. Print students with grade ≥ 80
# #3. Find the oldest student
# #4. Calculate average grade
# #5. Count students
# # Without using len().
students = [
    {"name":"Ravi","age":20,"grade":85},
    {"name":"Priya","age":19,"grade":92},
    {"name":"Arjun","age":21,"grade":78}
]
for student in students:
    print(student['name'])

print(list(filter(lambda s: s['grade'] >= 80, students)))

print(max(students, key = lambda s: s['age']))

avg = sum(map(lambda s: s['grade'], students)) / len(students)
print(avg)

count = 0
for student in students:
    count+=1
print(count)    

# #dict of lists
students = [
    {"name":"Ravi","section":"A"},
    {"name":"Priya","section":"B"},
    {"name":"Arjun","section":"A"},
    {"name":"Neha","section":"C"},
    {"name":"Rahul","section":"B"}
]

# #Group Students by Section
grouped = {}
for student in students:
    grouped.setdefault(student['section'], []).append(student)
print(grouped)    

# #only name
grouped = {}
for student in students:
    grouped.setdefault(student['section'], []).append(student['name'])
print(grouped)

students = [
    {"name":"A","grade":80},
    {"name":"B","grade":90},
    {"name":"C","grade":80},
    {"name":"D","grade":95},
    {"name":"E","grade":90}
]

count = {}
for student in students:
    grade = student['grade']

    if grade in count:
        count[grade] +=1
    else:
        count[grade] = 1

for grade in count:
    if count[grade] > 1:
        print(grade)

# #flatten nested lists
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

flat = []
for rows in matrix:
    for item in rows:
        flat.append(item)

print(flat)


data = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
al = [v for d in data for v in d.values()]
print(al)
#problem
students = [
    {"name": "Ravi", "grade": 88, "section": "A"},
    {"name": "Priya", "grade": 91, "section": "B"},
    {"name": "Arjun", "grade": 88, "section": "A"},
    {"name": "Meera", "grade": 76, "section": "B"},
    {"name": "Sara", "grade": 91, "section": "A"},
]

# In under 30 lines, without any library imports:
# 1. Sort all students by grade, descending
sorted_students = sorted(students, key = lambda s: s['grade'] , reverse = True)
print(sorted_students)
# 2. Group students by section into {section: [names]}
grouped = {}
for student in students:
    grouped.setdefault(student['section'], []).append(student['name'])
print(grouped)
# 3. Find any duplicate grades and which students share them
dup = {}
for student in students:
    grade = students['grade']

    if grade in students:
        dup +=1
    else:
        dup = 1
print(dup)            
# 4. Print a formatted summary:
#    Section A: Ravi (88), Arjun (88), Sara (91)
#    Section B: Priya (91), Meera (76)
#    Duplicate grades: 88 (Ravi, Arjun), 91 (Priya, Sara)