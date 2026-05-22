names = 'Harry' , 'Hermoine' , 'Ron', 'George', 'Fred' , 'Neville' , 'Luna', 'Ginny', 
'Parvati','Padma', 'Hannah', 'Lavender'
count = {}
for name in names:
    first = name[0]
    count[first] = count.get(first,0) + 1
print(count)

