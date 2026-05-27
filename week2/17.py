#sets 
cs_courses = {'OS', 'DBMS', 'Python', 'Math'}
art_courses = {'Art', 'Design','Math'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

cs_courses.add('C++')
print(cs_courses)

cs_courses.add('OS')
print(cs_courses)

l = [x for x in range(100)]

look = 98
for i,el in enumerate(l):
    if el == look:
        print('exists')
# O(n) 

s = {x for x in range(100)}
lookk = 98
print(lookk in s)
# O(1)

li = [1,1,1,2,4,5,5]
dup = len(set(s)) != len(s)
print(dup)

s = {1,1,1,2,4,5,5}
s.add(1)
s.remove(5)
s.discard(2)
print(s)