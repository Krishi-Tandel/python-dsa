# largest of 3 numbers
a = int(input("Enter 1st digit"))
b = int(input("Enter 2nd digit"))
c = int(input("Enter 3rd digit"))
if a>b:
    if a>c:
        print("1st digit is largest:", a)
    else:
        print("3rd digit is largest:",c)
if b>c:
    print("2nd digit is largest")
else:
    print("3rd digit is largest")
                          