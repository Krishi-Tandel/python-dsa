#day 2 concepts
#Build a simple login check: set a correct username and password. Ask the user to enter both. Print a specific message for: wrong username only, wrong password only, both wrong, or successful login.
username = 'Jeet'
password = 1234

user_name = input("Enter your username: ")
pass_word = int(input("Enter your password: "))

if user_name != username and pass_word == password:
    print("incorrect username")
elif user_name == username and pass_word != password:
    print("Incorrect password")   
elif user_name != username and pass_word != password:
    print("Incorrect username and password")     
else:
    print("login successfull")