#Day 2 concepts 
#Write a grade classifier: given a score (0–100), print "A" (90+), "B" (80–89), "C" (70–79), "D" (60–69), or "F" (below 60).

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("Your grade is A")
elif grade > 80 and grade<89:
    print("Your grade is B")
elif grade>70 and grade<79:
    print("Your grade is C") 
elif grade>60 and grade<69:
    print("Your grade is D")
else:
    print("Your grade is F")               