#nested condtion
#leap year using nested condtions only
n = int(input("Enter Year:"))
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year") 
    else:
        print("Leap year") 
else:
    print("Not a leap year")                  