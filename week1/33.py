'''
Create variables for a rectangle's length and width. 
 Using only those two variables and operators, calculate and print: area, perimeter, 
and whether it's a square (True/False).
'''
width = float(input("Enter width: "))
length = float(input("Enter length: "))
area = width * length
perimeter = 2 * (width + length)
print("Area is: ",area)
print("Perimeter is: ",perimeter)
if width == length:
    print("Square")
else:
    print("Not a square")    