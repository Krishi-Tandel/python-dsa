#nested condition
#classify number
n = int(input("Enter digit"))
if n>0:
    if n % 2 == 0:
        print("Number is positive and even:", n)
    else:
        print("Number is positive and odd:", n)
elif n == 0:
    print("Number is zero:",n) 
else:
    print("Number is negative:",n)               
 