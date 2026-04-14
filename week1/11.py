# nested 
a = input("Enter your username:")
b = input("Enter your password:")

if a == "abc":
    if b == "a123":
        print("Login success")
    else:
        print("Password incorrect")
else:
    print("Username incorrect.")            