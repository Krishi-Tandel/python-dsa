#tuple 
#literals
tup = (1,2)
tup1 = 1,2 #tuple packing
t = (1,) #single element tuple

#tuple constructor
a = tuple(1,2)
#empty tuple
a = tuple()

# #swap without temp
a = 5
b = 10
(print(a,b))
(a,b) = (b,a)
print(a,b)
# #tuples with multiple datatypes
student_course = ('Krishi',20, ['python','react'])
print(student_course)
# #in a tuple, elements are immutable but if tuple contains a list, it can be mutated
student_course[2][0] = 'JavaScript'
print(student_course)



num = (1,2,3,4,5)
#reversing a tuple
print(tuple(reversed(num)))
print(num[::-1])
#unpacking tuples 
a,b,c,d,e = num
print(a)
print(b)

# #packing tuples
num = b,c,d
print(num)

#*
num = (1,2,3,4,5) #if num of variables do not match elements inside tuple, it raises an error
first, *middle, last = num
print(first)
print(middle)
print(last)

print(type(middle))  # a list

#merging tuple
name = ('J',)
contact = ('j@gmail.com','0000')
print(*name, *contact)

#tuples as dict keys
d = {
    ('k','j') : 20,
    # [('k','j')] : 21,  a tuple that is a list cannot be a dict key
}
print(d)


#named tuple
from collections import namedtuple
Color = namedtuple('color',['red','green','blue'])
color = Color(255,55,55)
print(color.blue)
white = Color(255,255,255)
print(white.red)

#namedtuples are more readable than normal tuples and has less code than dictionaries