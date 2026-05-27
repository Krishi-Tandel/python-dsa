registered_users = {"Alice", "Bob", "Charlie", "Diana", "Linda"}
checked_in_users = {"Alice", "Charlie", "Linda"}

registered_users |= {'Krishi'}
print(id(checked_in_users))

print(registered_users - checked_in_users)
print(checked_in_users - registered_users)

