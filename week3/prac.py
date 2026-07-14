class BankAccount:
    no_of_acc = 0

    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance
        self.history = []
        BankAccount.no_of_acc += 1
    
    @property
    def balance(self):
        return self._balance 
    
    @balance.setter
    def balance(self,value):
        if value <= 0:
            raise ValueError('Balance cannot be negative')
        self._balance = value

    @balance.deleter
    def balance(self):
        del self._balance
        print('Deleted balance')

    def deposit(self,amount):
        if amount <= 0:
            print('Amount must be positive')

            return
        self.balance += amount
        self.history.append(f'Deposited: {amount}')
       
    def withdraw(self,amount):
        if amount <= 0:
            print('Amount must be positive')
        if amount > self.balance:
            print('Insufficient balance')
            return 
        self.balance -= amount
        self.history.append(f'Withdrew: {amount}')

    def transfer(self,other_acc,amount):
        if amount <= 0:
            print('Amount must be positive')
        if amount > self.balance:
            print('Insufficient balance')
            return 
        self.balance -= amount
        other_acc.balance += amount

        self.history.append(f'Transferred {amount} to {other_acc.owner}')
        other_acc.history.append(f'Received {amount} from {self.owner}')

    def show_details(self):
        for entries in self.history:
            print(entries)

    @staticmethod
    def cal_interest(amount,rate):
        return amount * rate / 100
    
    @classmethod
    def from_string(cls,text):
        owner,balance = text.split(',')
        return cls(owner,int(balance))

# Create accounts
acc1 = BankAccount("Krishi", 5000)
acc2 = BankAccount("Rahul", 3000)

print("Owner:", acc1.owner)
print("Balance:", acc1.balance)

print("-" * 40)

# Deposit
acc1.deposit(2000)
print("After deposit:", acc1.balance)

print("-" * 40)

# Withdraw
acc1.withdraw(1000)
print("After withdrawal:", acc1.balance)

print("-" * 40)

# Transfer
acc1.transfer(acc2, 1500)

print("Krishi Balance:", acc1.balance)
print("Rahul Balance:", acc2.balance)

print("-" * 40)

# Transaction history
print("Krishi History")
acc1.show_details()

print()

print("Rahul History")
acc2.show_details()

print("-" * 40)

# Static method
interest = BankAccount.cal_interest(10000, 7)

print("Interest:", interest)

print("-" * 40)

# Class method
acc3 = BankAccount.from_string("Anjali,8000")

print(acc3.owner)
print(acc3.balance)

print("-" * 40)

# Class variable
print("Total Accounts:", BankAccount.no_of_acc)

print("-" * 40)

# Setter
acc1.balance = 9000
print("Updated Balance:", acc1.balance)

print("-" * 40)

# Deleter
del acc1.balance

# Uncomment to see the error after deletion
# print(acc1.balance)
