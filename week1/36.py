'''
Password retry system:
Max 3 attempts
After that → “Account locked”
'''
correct_password = "1234"
tries = 0
while tries<3:
    password = input("Enter password: ")
    if password== correct_password:
        print("Correct password ")
        break
    else:
        tries+=1
        print(f"Incorrect password. Try again. Attempts left = {3-tries}")
if tries == 3:
    print("Account locked!")               
        