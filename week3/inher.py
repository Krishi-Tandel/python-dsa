#Person → Student → GraduateStudent: Use super() in each __init__, override a display_info() method,
#  and verify isinstance() and issubclass() results.

class Person:

    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'

    def display_info(self):
        return f'{self.first} {self.last}'

class Student(Person):

    def __init__(self,first,last,enroll_no):
        super().__init__(first,last)
        self.enroll_no = enroll_no

class GraduateStudent(Student):
    
    def __init__(self,first,last,enroll_no,cgpa):
         super().__init__(first,last,enroll_no)
         self.cgpa = cgpa

    def display_info(self):
        return f'{super().display_info()} ---> {self.cgpa}'
    
s = Person('Krishi','Tandel')
print(s.email)

print(s.display_info())

s1 = GraduateStudent('Jeet','Tandel',101,9.04)

print(s1.email)
print(s1.display_info())

print(isinstance(s1, Person))

print(issubclass(Person, GraduateStudent))