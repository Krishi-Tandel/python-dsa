class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{} @gmail.com'.format(self.first, self.last)
    def fullname(self):
        return f'{self.first} {self.last} '
    
    def __str__(self):
        return f'{self.fullname()}: {self.pay}'
    
    def __repr__(self):
        return '{}-{}'.format(self.fullname(),self.email)
    
    def __len__(self):
        return len(self.fullname())
    
    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee('Krishi','Tandel', 20000)
emp2 = Employee('Jeet','Tandel',20000) 

print(emp1.__str__())
print(emp1.__repr__())

print(len(emp2))
print(emp1 + emp2)