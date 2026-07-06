class Employe:
    pass       #empty class

emp1 = Employe
emp2 = Employe

emp1.first = 'Jeet'
emp1.last = 'Tandel'
emp1.pay = 50000

emp2.first = 'Krishi'
emp2.last = 'Tandel'
emp2.pay = 45000

class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

em1 = Employee('Jeet','Tandel', 50000)    
em2 = Employee('Krishi' ,'Tandel',50000)
print(em1.first)
 
#action

class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
    def fullname(self):
        return '{} {} '.format(self.first, self.last)   
em1 = Employee('Jeet','Tandel', 50000)    
em2 = Employee('Krishi' ,'Tandel',50000)
print(em1.pay)
print(Employee.fullname(em2))
print(em1.fullname())