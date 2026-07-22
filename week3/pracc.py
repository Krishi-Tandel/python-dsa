'''
Write a class with __eq__, __lt__, __add__, __len__, __contains__, __iter__
Write an abstract base class with @abstractmethod and two concrete subclasses
Write a function that works on any object with a speak() method — demonstrate duck typing
Sort a list of your custom objects using sorted() — must work via __lt__
'''
class Num:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __eq__(self, value):
        return self.a == value.a and self.b == value.b
    
    def __lt__(self, other):
        return (self.a,self.b) < (other.a, other.b)
        
    def __add__(self, other):
        return Num(self.a + other.a and self.b + other.b) 
    
    def __iter__(self):
        return iter(self.a, self.b)
    
    def __len__(self):
        return 2
    
    def __contains__(self, item):
        return item in (self.a, self.b)
    
    def __str__(self):
        return f'({self.a}), ({self.b})'

nums = [
    Num(3, 4),
    Num(1, 8),
    Num(2, 5),
    Num(1, 2)
]

sorted_nums = sorted(nums)

for n in sorted_nums:
    print(n.a, n.b)
    
import math    
from abc import ABC, abstractmethod
class Shape(ABC):

    def __init__(self,color):
        self.color = color

    @abstractmethod 
    def area(self):
        raise NotImplementedError
    
    @abstractmethod
    def perimeter(self):
        raise NotImplementedError
  
class Circle(Shape):
    
    def __init__(self, color,radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
      
class Rectangle(Shape):
    
    def __init__(self, color,length, breadth):
        super().__init__(color)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
c = Circle('blue',12)
print(c.area())
print(c.perimeter())

r = Rectangle('red',12,11)
print(r.area())
print(r.perimeter())


class Dog:

    def speak(self):
        print('Barks')

class Cat:

    def speak(self):
        print('Meows')

def make_sound(obj):
    obj.speak()

make_sound(Dog())
make_sound(Cat())