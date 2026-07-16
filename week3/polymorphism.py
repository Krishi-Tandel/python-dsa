class Animal:

    def speak(self):
        raise NotImplementedError
    
class Dog(Animal):

    def speak(self):
        print('Woof!')

class Cat(Animal):

    def speak(self):
        print('Meow!')

c= Cat()
d = Dog()

c.speak()
d.speak()


# polymorphism with inheritance 
Animal = [
    Dog(),
    Cat()
]

for animal in Animal:
    animal.speak()


#duck typing
class Cow:
    def speak(self):
        print('Moo')

class Robot:
    def speak(self):
        print('Beep')

def make_sound(obj):
    obj.speak()

make_sound(Cow())
make_sound(Robot())
