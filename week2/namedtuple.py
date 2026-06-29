# namedtuple
from collections import namedtuple
Point = namedtuple('Point',['x y'], default = [0])
point = Point(2)

print(point.x)


# Person = namedtuple('Person','name , age , height')
# print(Person._make(['Jeet',22,5.9]))


#default arguments
# P = namedtuple('P',['x','y'])
# p = P(2,5)

# print(p.y)

