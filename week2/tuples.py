# Given a list of (student_name, subject) tuples
# count how many times each (name, subject) pair appears
records = [
    ("Ravi", "Math"), ("Priya", "Science"),
    ("Ravi", "Math"), ("Arjun", "Math"),
    ("Priya", "Science"), ("Ravi", "Science")
]
# expected: {("Ravi", "Math"): 2, ("Priya", "Science"): 2, ...}
# use tuple as dict key — build frequency counter

dic = dict()

for record in records:
    if record in dic:
       dic[record] += 1
    else:
        dic[record] = 1
        
print(dic)    

