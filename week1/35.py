'''
Capstone: ATM simulator. Set a starting balance. 
Loop a menu: 1) Check balance  2) Deposit  3) Withdraw  4) Exit. 
Validate that withdrawals don't exceed the balance. 
Count total transactions and show the count on exit.
'''
balance = 1000
operation = ""
correct_pin = 1234
transaction = 0
while True:
    pin = int(input("Please enter pin to continue ")) 
    if pin != correct_pin:
        print("Wrong pin. Try Again: ")
    else:
        print("Correct pin")   
        while operation != "4" and pin == correct_pin:
            operation = input("""Choose an operation
1) Check balance
2) Deposit
3) Withdraw
4) Exit
""")
            if operation == "2":
                amount = int(input("Enter amount to be deposited: "))
                balance += amount
                print("Amount deposited successfully!")
                transaction +=1
        
            elif operation == "3":
                amount = int(input("Enter amount to withdraw: "))
                balance -= amount
                print("Amount withdrawn")
                transaction +=1
    
            elif operation == "1":
                print(balance)
                transaction +=1
            elif operation == "4":
                print("Total transaction: ",transaction)
                break
            else:
                print("Invalid Choice")
