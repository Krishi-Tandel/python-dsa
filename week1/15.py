# numbers upto n
n = int(input("Enter n: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()

# even numbers upto n
n = int(input("\nEnter n: "))
i = 2
while i <= n:
    print(i, end=" ")
    i += 2
print()

# odd numbers upto n
n = int(input("\nEnter n: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 2
print()

# sum of first n numbers
n = int(input("\nEnter n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum:", total)

# multiplication table
n = int(input("\nEnter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1