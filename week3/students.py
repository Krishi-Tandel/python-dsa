'''
class Student:
    def __init__(self, name, grade, subjects):
        self.name = name
        self.grade = grade            # int 0-100
        self.subjects = subjects      # list of subject names

    # implement all of these:
    # __str__    → "Ravi (88) — Math, Science, English"
    # __repr__   → "Student(name='Ravi', grade=88)"
    # __len__    → number of subjects
    # __eq__     → equal if same name and grade
    # __lt__     → compare by grade
    # __add__    → combine two students' subject lists, return new Student
    #              with both names and average grade
    # __contains__ → check if a subject name is in self.subjects
    # __iter__   → iterate over subjects

students = [
    Student("Ravi", 88, ["Math", "Science"]),
    Student("Priya", 91, ["English", "History", "Math"]),
    Student("Arjun", 75, ["Science", "Math", "PE"]),
]

# after building, these must all work:
print(sorted(students))           # sort by grade using __lt__
print("Math" in students[0])      # __contains__
print(len(students[1]))           # __len__
for subj in students[2]:          # __iter__
   print(subj)
'''
class Student:

    def __init__(self,name,grade,subjects):
        self.name = name
        self.grade = grade
        self.subjects = list(subjects)

    def __str__(self):
        return f'{self.name} ({self.grade}) - {','.join(self.subjects)}'
        
    def __repr__(self):
        return f"Student(name = '{self.name}', grade = {self.grade})"
    
    def __len__(self):
        return len(self.subjects)
    
    def __eq__(self,other):
        return self.name == other.name and self.grade == other.grade
    
    def __lt__(self,other):
        return self.grade < other.grade
    
    def __add__(self, other):
       new_name = f'{self.name} & {other.name}'
       new_grade = (self.grade + other.grade) //2
       new_sub = self.subjects + other.subjects
       return(new_name,new_grade,new_sub)

    def __contains__(self, item):
        return item in self.subjects
    
    def __iter__(self):
        return iter(self.subjects)

students = [
    Student("Ravi", 88, ["Math", "Science"]),
    Student("Priya", 91, ["English", "History", "Math"]),
    Student("Arjun", 75, ["Science", "Math", "PE"]),
]
print(sorted(students))           # sort by grade using __lt__
print("Math" in students[0])      # __contains__
print(len(students[1]))           # __len__
for subj in students[2]:          # __iter__
   print(subj)