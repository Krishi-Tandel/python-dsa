# class Movie:

#     def __init__(self,title, rating):
#         self.title = title
#         self.rating = rating

#     def is_hit(self,rating):
#         if rating >= 8:
#             return True
#         return False


# mv1 = Movie('Harry Potter and the Philospher"s stone', 9)

# print(mv1.is_hit(9))



class BankAccount:
    num_of_acc = 0

    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        BankAccount.num_of_acc += 1

acc1 = BankAccount('Rahul',2000)
acc2 = BankAccount('Priya',3000)

print(BankAccount.num_of_acc)

