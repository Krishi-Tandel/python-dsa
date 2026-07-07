# class Emoployee:

#     def __init__(self, first,last):
#         self.first = first
#         self.last = last
#         self.email = '{} {}@gmail.com'.format(self.first, self.last)
    
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

# emp1 = Emoployee('Jeet','Tandel')

# emp1.fullname = 'Krishi Tandel' # will give error so we use setter

# print(emp1.first)
# print(emp1.fullname())

class Emoployee:

    def __init__(self, first,last):
        self.first = first
        self.last = last
        self.email = '{} {}@gmail.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Deleted!')

emp1 = Emoployee('Jeet','Tandel')

print(emp1.first)
print(emp1.fullname)

emp1.fullname = 'Krishi Tandel' 

print(emp1.first)
print(emp1.fullname)

del emp1.fullname