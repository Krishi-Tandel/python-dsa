'''
Multiplication Table as Nested List
Use a nested list comprehension to build a 5x5 multiplication table as a list of lists.
Then print it in grid format using a nested for loop.
'''
table = [[i*j for j in range(1,6)] for i in range(1,6)]
print(table)
for row in table:
    for value in row:
        print(value,end = "\t")
    print()        